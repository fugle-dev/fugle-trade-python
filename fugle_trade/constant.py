from enum import Enum

class Action(str, Enum):
    Buy = "B" #買
    Sell = "S" #賣


class APCode(str, Enum):
    Common = "1" #整股
    AfterMarket= "2" #盤後
    Odd = "3" #盤後零股
    Emg = "4" #興櫃
    IntradayOdd = "5" #盤中零股

class Trade(str, Enum):
    Cash = "0" #現股
    Margin = "3" #融資
    Short = "4" #融券
    DayTrading = "9" #自動當沖
    DayTradingSell = "A" #現股當沖賣

class PriceFlag(str, Enum):
    Limit = "0" #限價
    Flat = "1" #平盤
    LimitDown = "2" #跌停
    LimitUp = "3" #漲停
    Market = "4" #市價

class BSFlag(str, Enum):
    FOK = "F"
    IOC = "I"
    ROD = "R"
