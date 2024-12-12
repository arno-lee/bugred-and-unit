from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Framework.NavBar import NavBar
from Framework.Utils.Browser import Browser


class UserProfile:
  def __init__(self):
    self._user_name_entry_loc = (By.XPATH, '//td[text()="ФИО"]/../td[2]')
    self._email_entry_loc = (By.XPATH, '//td[text()="Email"]/../td[2]')
    self._phone_entry_loc = (By.XPATH, '//td[text()="Телефон"]/../td[2]')
    self._user_profile_form_sel = "div.content"
    self._user_profile_form_loc = (By.CSS_SELECTOR, self._user_profile_form_sel)

    browser = Browser()
    user_profile_form_all_loc = (By.CSS_SELECTOR, self._user_profile_form_sel + " > *")
    browser.wait.until(EC.presence_of_all_elements_located(user_profile_form_all_loc))

    self._user_profile_form = browser.instance.find_element(*self._user_profile_form_loc)

  @property
  def user_name(self):
    return self._user_profile_form.find_element(*self._user_name_entry_loc)
  
  @property
  def email(self):
    return self._user_profile_form.find_element(*self._email_entry_loc)
  
  @property
  def phone(self):
    return self._user_profile_form.find_element(*self._phone_entry_loc)
  
  @property 
  def nav_bar(self):
    return NavBar()
    
    