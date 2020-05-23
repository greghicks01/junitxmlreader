from dynaconf import LazySettings
from dynaconf.loaders.ini_loader import load

INI = """
a = 'a,b'
[default]
password = '@int 99999'
host = "server.com"
port = '@int 8080'
alist = item1, item2, '@int 23'
  [[service]]
  url = "service.com"
  port = '@int 80'
    [[[auth]]]
    password = "qwerty"
    test = '@int 1234'
[development]
password = '@int 88888'
host = "devserver.com"
[production]
password = '@int 11111'
host = "prodserver.com"
[global]
global_value = 'global'
"""

INI2 = """
[global]
secret = "@float 42"
password = '@int 123456'
host = "otherini.com"
"""

INIS = [INI, INI2]
settings = LazySettings(ENV_FOR_DYNACONF="PRODUCTION")

load(settings, filename='config.ini')
assert settings.test_rail_url == "https://greghicks.testrail.io"
