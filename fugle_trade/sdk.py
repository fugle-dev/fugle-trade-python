"""
Expose as a single library for user to use

"""
from fugle_trade_core.fugle_trade_core import CoreSDK
from fugle_trade.constant import APCode, PriceFlag
from fugle_trade.order import OrderObject
from fugle_trade.websocket import WebsocketHandler
from fugle_trade.util import (
    ft_check_password,
    ft_get_password,
    ft_set_password,
    setup_keyring,
)
from json import loads


class SDK:
    """Main sdk for fugleTrade"""

    def __init__(self, config):
        self.validate_config(config)
        self.__ip = ""
        self.__AID = config["User"]["Account"]

        if not self.__AID:
            raise TypeError("please setup your config before using this SDK")
        setup_keyring(self.__AID)
        ft_check_password(self.__AID)

        self.__core = CoreSDK(
            config["Core"]["Entry"],
            config["User"]["Account"],
            config["Cert"]["Path"],
            ft_get_password("fugle_trade_sdk:cert", self.__AID),
            config["Api"]["Key"],
            config["Api"]["Secret"],
        )
        self.__wsHandler = WebsocketHandler()

    def validate_config(self, config):
        if not (
            config.has_section("Core")
            and config.has_section("Cert")
            and config.has_section("Api")
            and config.has_section("User")
        ):
            raise TypeError("please fill in config file")
        if not config["Core"].get("Entry"):
            raise TypeError("please give Core Entry value")
        if config["Core"].get("Environment"):
            if (
                config["Core"]["Environment"].lower() == "simulation"
                and config["Core"]["Entry"].find("simulation") == -1
            ):
                raise TypeError("Entry and Environment conflict")

        if (not config["Cert"].get("Path")) or config["Cert"]["Path"].find(
            ".p12"
        ) == -1:
            raise TypeError("please give correct Cert Path")

        if (not config["Api"].get("Key")) or (not config["Api"].get("Secret")):
            raise TypeError("please give correct Api Key and Secret")

        if not config["User"].get("Account"):
            raise TypeError("please give correct User Account")

    def certinfo(self):
        return loads(self.__core.get_certinfo())

    def reset_password(self):
        ft_set_password(self.__AID)
        print("reset_password done!!")

    def place_order(self, order_object: OrderObject):
        """place order"""
        return loads(self.__core.order(order_object))["data"]

    def delete_order(self, order_result):
        """delete_order"""
        print(
            "*** important: this function will be deprecated in next version, please use cancel_order instead ***"
        )
        return loads(self.__core.modify_volume(order_result, 0))["data"]

    def cancel_order(self, in_order_result, **kwargs):
        """cancel_order"""
        order_result = self.recover_order_result(in_order_result)
        apcode = str(order_result["ap_code"])
        unit = self.__core.get_volume_per_unit(order_result["stock_no"])
        excuted_celqty = None

        if "cel_qty" in kwargs and "cel_qty_share" in kwargs:
            raise TypeError("cel_qty or cel_qty_share, not both")

        # if no args, treat it as cancel all
        if "cel_qty" not in kwargs and "cel_qty_share" not in kwargs:
            return loads(self.__core.modify_volume(order_result, 0))["data"]

        if "cel_qty" in kwargs:
            if apcode in (APCode.Odd, APCode.Emg, APCode.IntradayOdd):
                excuted_celqty = kwargs["cel_qty"] * unit
            else:
                excuted_celqty = kwargs["cel_qty"]

        if "cel_qty_share" in kwargs:
            if apcode in (APCode.Odd, APCode.Emg, APCode.IntradayOdd):
                excuted_celqty = kwargs["cel_qty_share"]
            else:
                if kwargs["cel_qty_share"] % unit != 0:
                    raise TypeError("must be multiplys of " + str(unit))
                excuted_celqty = int(kwargs["cel_qty_share"] / unit)

        if not excuted_celqty:
            raise TypeError("must provide cel_qty or cel_qty_share")

        return loads(self.__core.modify_volume(order_result, excuted_celqty))["data"]

    def modify_price(
        self, in_order_result, target_price=None, price_flag=PriceFlag.Limit
    ):
        """modify_price"""
        if target_price == None and price_flag == None:
            raise TypeError("must provide valid arguments")

        if price_flag != None:
            if type(price_flag) is not PriceFlag:
                raise TypeError("Please use fugleTrade.constant PriceFlag")
            price_flag = price_flag.value

        order_result = self.recover_order_result(in_order_result)
        return loads(self.__core.modify_price(order_result, target_price, price_flag))[
            "data"
        ]

    def get_order_results(self):
        """get order result data 取得當日委託明細"""
        order_res = self.__core.get_order_results()
        return loads(order_res)["data"]["order_results"]

    def get_order_results_by_date(self, start, end):
        """get order result data by date 用日期當作篩選條件委託明細"""
        order_res_history = self.__core.get_order_result_history("0", start, end)
        return loads(order_res_history)["data"]["order_result_history"]

    def get_transactions(self, query_range):
        """get transactions data 成交明細"""
        transactions_res = self.__core.get_transactions(query_range)
        return loads(transactions_res)["data"]["mat_sums"]

    def get_transactions_by_date(self, start, end):
        """用日期當作篩選條件 get transactions data by date 成交明細"""
        transactions_res = self.__core.get_transactions_by_date(start, end)
        return loads(transactions_res)["data"]["mat_sums"]

    def get_inventories(self):
        """get inventories data 庫存資訊"""
        inventories_res = self.__core.get_inventories()
        return loads(inventories_res)["data"]["stk_sums"]

    def get_balance(self):
        """get balance data 餘額資訊"""
        inventories_res = self.__core.get_balance()
        return loads(inventories_res)["data"]

    def get_trade_status(self):
        """get trade status 交易狀態資訊"""
        inventories_res = self.__core.get_trade_status()
        return loads(inventories_res)["data"]

    def get_market_status(self):
        """get market status 市場開盤狀態資訊"""
        inventories_res = self.__core.get_market_status()
        return loads(inventories_res)["data"]

    def get_settlements(self):
        """get settlement data 交割資訊"""
        settlements_res = self.__core.get_settlements()
        return loads(settlements_res)["data"]["settlements"]

    def login(self):
        """login function"""
        self.__core.login(
            self.__AID, ft_get_password("fugle_trade_sdk:account", self.__AID)
        )

    def get_key_info(self):
        """key info"""
        key_info_res = self.__core.get_key_info()
        return loads(key_info_res)["data"]

    def get_machine_time(self):
        key_info_res = self.__core.get_machine_time()
        return loads(key_info_res)["data"]

    def on(self, param):
        def inner(func):
            """
            do operations with func, register func into __wsHandler

            """
            self.__wsHandler.set_callback(param, func)
            return func

        return inner

    def connect_websocket(self):
        self.__wsHandler.connect_websocket(self.__core.get_ws_url())

    def recover_order_result(self, order_result):
        """recover true ord_qty value before send to api"""
        apcode = order_result["ap_code"]
        stockno = order_result["stock_no"]
        unit = self.__core.get_volume_per_unit(stockno)
        new_dict = {}
        for key, value in order_result.items():
            if key.endswith("qty"):
                if apcode in (APCode.Odd, APCode.Emg, APCode.IntradayOdd):
                    new_dict[key] = int(value * unit)
                else:
                    new_dict[key] = int(value)
        return {**order_result, **new_dict}
