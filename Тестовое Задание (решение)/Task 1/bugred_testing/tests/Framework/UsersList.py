from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.UserProfile import UserProfile
from Framework.Utils import Browser


class UsersList:
  def __init__(self, parent):
    self._email_cell_loc = lambda email: (By.XPATH, f"//td[text()='{email}']")
    self._table_empty_flag_loc = (By.XPATH, "//p[contains(text(), 'All:0')]")
    self._view_btn_loc = (By.XPATH, '//a[text()="Посмотреть"]')
    self._delete_btn_loc = (By.XPATH, '//a[text()="Удалить"]')
    self._users_list_loc = (By.CSS_SELECTOR, 'table.table')

    self._users_list = parent.find_element(*self._users_list_loc)

  def email_present(self, email):
    return self._users_list.find_elements(*self._email_cell_loc(email))

  def view_1st(self):
    self.view_btn_1st.click()
    return UserProfile()
  
  def delete_1st(self):
    self.delete_btn_1st.click()

  @property
  def view_btn_1st(self):
    return self._users_list.find_element(*self._view_btn_loc)
  
  @property
  def delete_btn_1st(self):
    return self._users_list.find_element(*self._delete_btn_loc)
  
  @property
  def table_empty(self):
    try:
      Browser().wait.until(EC.presence_of_element_located(self._table_empty_flag_loc))
      return False
    except:
      return True

