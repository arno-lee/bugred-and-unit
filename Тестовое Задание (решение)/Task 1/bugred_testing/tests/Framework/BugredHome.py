
from selenium.webdriver.common.by import By

from Framework.LogInForm import LogInForm
from Framework.Utils.Browser import Browser
from Framework.Utils.Config import Config


# Bugred home page
class BugredHome:
  def __init__(self):
    self._body_loc = (By.CSS_SELECTOR, "body")
    self._log_in_btn_loc = (By.CSS_SELECTOR, 'a[href="/user/login/index.html"]')

    config = Config()
    browser = Browser()

    browser.instance.get(config.urls.url)
    browser.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    
    self._body = browser.instance.find_element(*self._body_loc)

  @property
  def log_in_btn(self):
    return self._body.find_element(*self._log_in_btn_loc)

  def log_in_form(self):
    self.log_in_btn.click()
    return LogInForm()

