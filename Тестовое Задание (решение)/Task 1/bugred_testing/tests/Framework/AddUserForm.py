from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Framework.Utils.Browser import Browser


# Add user form
class AddUserForm:
  def __init__(self):
    self._gender_select_loc = (By.CSS_SELECTOR, "select[name='noibiz_gender']")
    self._hobby_input_loc = (By.CSS_SELECTOR, "textarea[name='noibiz_hobby']")
    self._field_name_loc = lambda name: (By.CSS_SELECTOR, f"input[name='noibiz_{name}']")
    self._name_input_loc = (By.CSS_SELECTOR, "input[name='noibiz_name']")
    self._email_input_loc = (By.CSS_SELECTOR, "input[name='noibiz_email']")
    self._password_input_loc = (By.CSS_SELECTOR, "input[name='noibiz_password']")
    self._start_date_input_loc = (By.CSS_SELECTOR, "input[name='noibiz_date_start']")
    
    self._add_user_btn_loc = (By.CSS_SELECTOR, "input[type='submit'][name='act_create']")
    self._add_user_form_sel = "div.content"
    self._add_user_form_loc = (By.CSS_SELECTOR, self._add_user_form_sel)

    self._browser = Browser()
    add_user_form_all_loc = (By.CSS_SELECTOR, self._add_user_form_sel + " > *")
    self._browser.wait.until(EC.presence_of_all_elements_located(add_user_form_all_loc))

    self._add_user_form = self._browser.instance.find_element(*self._add_user_form_loc)

  def add_multiple_fields(self, field_data):
    for field_name, value in field_data.items():
        if field_name == "gender":
          selector = Select(self._add_user_form.find_element(*self._gender_select_loc))
          selector.select_by_visible_text(value)
        elif field_name == "hobby":
          field = self._add_user_form.find_element(*self._hobby_input_loc)
          field.send_keys(value)
        elif field_name == "avatar":
          continue
        elif field_name == "fathername1":
          continue # non-interactable 
        else:
          try: 
            field_loc = self._field_name_loc(field_name)
            field = self._add_user_form.find_element(*field_loc)
            field.send_keys(value)
          except:
            pass
    self.add_user_btn.click()

  def add_basic_user(self, name, email, password):
    self.name_input.send_keys(name)
    self.email_input.send_keys(email)
    self.password_input.send_keys(password)
    self.add_user_btn.click()
    self._browser.wait.until(EC.invisibility_of_element(self._add_user_form))

  @property
  def name_input(self):
    return self._add_user_form.find_element(*self._name_input_loc)
  
  @property
  def email_input(self):
    return self._add_user_form.find_element(*self._email_input_loc)
  
  @property
  def password_input(self):
    return self._add_user_form.find_element(*self._password_input_loc)

  @property
  def add_user_btn(self):
    return self._add_user_form.find_element(*self._add_user_btn_loc)