from configparser import ConfigParser
from fugle_trade.init import InitSDK

config = ConfigParser()
config.read('./config.ini')

initSDK = InitSDK(config)
initSDK.set_password()
