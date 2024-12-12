from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.Utils.Browser import Browser
from Framework.UsersHome import UsersHome


class LogInForm:
  def __init__(self):
    self._username_input_loc = (By.CSS_SELECTOR, 'input[type="text"][name="login"]')
    self._password_input_loc = (By.CSS_SELECTOR, 'input[type="password"][name="password"]')
    self._log_in_btn_loc = (By.CSS_SELECTOR, 'input.btn.btn-danger[type="submit"]')
    self._log_in_form_sel = 'form[action="/user/login/index.html"]'
    self._log_in_form_loc = (By.CSS_SELECTOR, self._log_in_form_sel)

    browser = Browser()
    log_in_form_all_loc = (By.CSS_SELECTOR, self._log_in_form_sel + " > *")
    browser.wait.until(EC.presence_of_all_elements_located(log_in_form_all_loc))

    self._log_in_form = browser.instance.find_element(*self._log_in_form_loc)
    
  def log_in(self, username, password):
    self.username_input.send_keys(username)
    self.password_input.send_keys(password)
    self.log_in_btn.click()
    return UsersHome()

  @property
  def username_input(self):
    return self._log_in_form.find_element(*self._username_input_loc)
  
  @property
  def password_input(self):
    return self._log_in_form.find_element(*self._password_input_loc)
  
  @property
  def log_in_btn(self):
    return self._log_in_form.find_element(*self._log_in_btn_loc)
    