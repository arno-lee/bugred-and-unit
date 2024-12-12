import json


class _EnclosedClass:
    def __init__(self, outer):
        self.outer = outer

# Configuration manager
class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path=None):
        if not hasattr(self, 'initialized'):  
            with open(config_path + "/options.json") as f:
                self._options = json.load(f)

            with open(config_path + "/urls.json") as f:
                self._urls = json.load(f)
            
            with open(config_path + "/credentials.json") as f:
                self._credentials = json.load(f)
            
            self.initialized = True
    
    @property
    def options(self):
        class _Options(_EnclosedClass):
            @property 
            def headless(self):
                return self.outer._options["headless"]
            
            @property 
            def wait_timeout(self):
                return self.outer._options["wait_timeout"]
            
        return _Options(self)
    
    @property
    def urls(self):
        class _Urls(_EnclosedClass):
            def __init__(self, outer):
                self.outer = outer

            @property 
            def url(self):
                return self.outer._urls["url"]
            
        return _Urls(self)
    
    @property
    def credentials(self):
        class _Credentials(_EnclosedClass):
            def __init__(self, outer):
                self.outer = outer

            @property 
            def user_email(self):
                return self.outer._credentials["user_email"]
            
            @property 
            def password(self):
                return self.outer._credentials["password"]
            
        return _Credentials(self)

