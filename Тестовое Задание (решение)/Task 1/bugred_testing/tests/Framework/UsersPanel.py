from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.AddUserForm import AddUserForm
from Framework.UsersList import UsersList
from Framework.Utils.Browser import Browser
from Framework.SearchUserForm import SearchUserForm


class UsersPanel:
  def __init__(self):
    self._add_user_btn_loc = (By.CSS_SELECTOR, 'a[href="/user/admin/index/create.html"]')
    self._users_panel_sel = "div.content"
    self._users_panel_loc = (By.CSS_SELECTOR, self._users_panel_sel)

    browser = Browser()
    users_panel_all_loc = (By.CSS_SELECTOR, self._users_panel_sel + " > *")
    browser.wait.until(EC.presence_of_all_elements_located(users_panel_all_loc))

    self._users_panel = browser.instance.find_element(*self._users_panel_loc)

  def add_user_form(self):
    self.add_user_btn.click()
    return AddUserForm()

  @property
  def add_user_btn(self):
    return self._users_panel.find_element(*self._add_user_btn_loc)
  
  @property
  def search_user_form(self):
    return SearchUserForm(self._users_panel)
  
  @property
  def users_list(self):
    return UsersList(self._users_panel)
  