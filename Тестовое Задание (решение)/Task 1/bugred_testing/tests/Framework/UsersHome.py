from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.Utils.Browser import Browser
from Framework.NavBar import NavBar
from Framework.UsersPanel import UsersPanel


class UsersHome:
  def __init__(self):
    self._users_home_sel = "body"
    self._users_home_loc = (By.CSS_SELECTOR, self._users_home_sel)

    browser = Browser()
    users_home_all_loc = (By.CSS_SELECTOR, self._users_home_sel + " > *")
    browser.wait.until(EC.presence_of_all_elements_located(users_home_all_loc))

    self._users_home = browser.instance.find_element(*self._users_home_loc)

  @property
  def users_panel(self):
    return UsersPanel()
  
  @property 
  def nav_bar(self):
    return NavBar()