"""
Define Order Objects
"""
import typing
from fugle_trade.constant import (
    Action,
    APCode,
    Trade,
    PriceFlag,
    BSFlag
)

class OrderObject():
    ap_code: APCode
    bs_flag: BSFlag
    price_flag: PriceFlag
    trade: Trade
    buy_sell: Action
    price: float
    stock_no: str
    quantity: int

    def __init__(
            self,
            buy_sell: Action,
            price: float,
            stock_no: str,
            quantity: int,
            ap_code: APCode = APCode.Common,
            bs_flag: BSFlag = BSFlag.ROD,
            price_flag: PriceFlag = PriceFlag.Limit,
            trade: Trade = Trade.Cash,
        ):

        if type(buy_sell) is not Action:
            raise TypeError("Please use fugleTrade.constant Action")

        # fugle_trade_core will check price format, no need to check price here

        if type(stock_no) is not str:
            raise TypeError("Please use type str in stockNo")

        if type(quantity) is not int:
            raise TypeError("Please use type int in quantity")
        elif ap_code == APCode.Common or ap_code == APCode.AfterMarket:
            if quantity < 1 or quantity > 500:
                raise TypeError("quantity must within range 1 ~ 499")

        elif ap_code == APCode.Odd or ap_code == APCode.IntradayOdd:
            if quantity < 1 or quantity > 1000:
                raise TypeError("quantity must within range 1 ~ 999")
        elif ap_code == APCode.Emg:
            if quantity < 1 or quantity > 499000 or (quantity > 1000 and quantity % 1000 != 0):
                raise TypeError("quantity must within range 1 ~ 499000, or multiply of 1000")

        if type(ap_code) is not APCode:
            raise TypeError("Please use fugleTrade.constant APCode")

        if type(bs_flag) is not BSFlag:
            raise TypeError("Please use fugleTrade.constant BSFlag")

        if type(price_flag) is not PriceFlag:
            raise TypeError("Please use fugleTrade.constant PriceFlag")

        if type(trade) is not Trade:
            raise TypeError("Please use fugleTrade.constant Trade")

        self.ap_code = ap_code
        self.price_flag = price_flag
        self.bs_flag = bs_flag
        self.trade = trade
        self.buy_sell = buy_sell
        self.price = price
        self.stock_no = stock_no
        self.quantity = quantity

    def __str__(self):
        return "ap_code: %s, price_flag: %s, bs_flag: %s, trade: %s, buy_sell: %s, price: %s, stock_no: %s, quantity: %s" % (self.ap_code, self.price_flag, self.bs_flag, self.trade, self.buy_sell, self.price, self.stock_no, self.quantity)
