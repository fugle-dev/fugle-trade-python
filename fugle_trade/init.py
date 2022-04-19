"""
Expose as a single library for user to use

"""
from fugle_trade_core.fugle_trade_core import CoreSDK
from fugle_trade.order import OrderObject
from fugle_trade.util import ft_check_password, ft_get_password, ft_set_password


class InitSDK:
    """Main sdk for fugleTrade"""
    def __init__(self, config):
        self.__ip = ""
        self.__AID = config['User']['Account']

    def set_password(self):
        ft_set_password(self.__AID)
        print("Done")
