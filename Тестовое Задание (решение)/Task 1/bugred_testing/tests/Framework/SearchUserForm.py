from selenium.webdriver.common.by import By


class SearchUserForm:
  def __init__(self, parent):
    self._search_user_input_loc = (By.CSS_SELECTOR, 'input[type="text"]')
    self._search_user_btn_loc = (By.CSS_SELECTOR, 'button[type="submit"]')
    self._search_user_form_loc = (By.CSS_SELECTOR, 'form[action="/user/admin/index"]')

    self._search_user_form = parent.find_element(*self._search_user_form_loc)

  def search_user(self, name_or_email):
    self.search_user_input.send_keys(name_or_email)
    self.search_user_btn.click()

  @property
  def search_user_input(self):
    return self._search_user_form.find_element(*self._search_user_input_loc)
  
  @property
  def search_user_btn(self):
    return self._search_user_form.find_element(*self._search_user_btn_loc)