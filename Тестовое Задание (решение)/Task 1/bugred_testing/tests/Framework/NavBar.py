from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.Utils.Browser import Browser


class NavBar:
  def __init__(self):
    self._user_menu_loc = (By.ID, "fat-menu")
    self._user_exit_item_loc = (By.CSS_SELECTOR, 'a[href="/user/logout.html"]')
    self._nav_bar_sel = "div.navbar"
    self._nav_bar_loc = (By.CSS_SELECTOR, self._nav_bar_sel)

    self._browser = Browser()
    nav_bar_all_loc = (By.CSS_SELECTOR, self._nav_bar_sel + " > *")
    self._browser.wait.until(EC.presence_of_all_elements_located(nav_bar_all_loc))
    
    self._nav_bar = self._browser.instance.find_element(*self._nav_bar_loc)

  def user_exit(self):
    self.user_exit_item.click()
    self._browser.wait.until(EC.invisibility_of_element(self._nav_bar))

  @property
  def user_menu(self):
    return self._nav_bar.find_element(*self._user_menu_loc)
  
  @property
  def user_exit_item(self):
    self.user_menu.click()
    return self._browser.wait.until(EC.presence_of_element_located(self._user_exit_item_loc))
