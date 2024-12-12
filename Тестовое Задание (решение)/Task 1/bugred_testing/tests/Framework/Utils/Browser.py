from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from Framework.Utils.Config import Config


# Browser singleton
class Browser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Browser, cls).__new__(cls)
        return cls._instance

    def __init__(self, browser=None):
        if not hasattr(self, 'initialized'):  
            self._config = Config()
            if self._config.options.headless:
                options = Options()
                options.add_argument("--headless") 
                self._instance._browser = browser(options=options)
            else:
                self._instance._browser = browser()

            self.initialized = True

    @property
    def wait(self):
        return WebDriverWait(self.instance, self._config.options.wait_timeout)
    
    @property
    def instance(self):
        return self._browser
    
    @classmethod
    def quit(cls):
        if cls._instance:
            cls._instance._browser.quit()
            cls._instance = None
