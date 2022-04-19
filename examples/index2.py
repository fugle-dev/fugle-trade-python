#from fugle_trade import sign_cert, login, get_order_result

from configparser import ConfigParser
import pprint
from fugle_trade.sdk import SDK
from fugle_trade.order import OrderObject
from fugle_trade.constant import (
    APCode,
    Trade,
    PriceFlag,
    BSFlag,
    Action
)

config = ConfigParser()
config.read('./config.ini')
pp = pprint.PrettyPrinter(indent=4)

sdk = SDK(config)

pp.pprint(sdk.get_machine_time())
sdk.login()

# order = OrderObject(
#     buySell = Action.Buy,
#     price = "45.20",
#     stockNo = "2942",
#     quantity = 499001,
#     apCode = APCode.Emg,
#     priceFlag = PriceFlag.Limit
# )

#pp.pprint(str(order))

pp.pprint(sdk.certinfo())
# pp.pprint(sdk.place_order(order))
# pp.pprint(sdk.get_key_info())
# pp.pprint(sdk.get_order_result())

# pp.pprint(sdk.get_inventories())

# pp.pprint(sdk.get_settlements())
# pp.pprint(sdk.get_transactions("1m"))

# print(sdk.get_machine_time())
# print(sdk.modify_volume(orderResult[2], celqty_share=1))
# sdk.delete_order(orderResult[0])
# orderResult = sdk.get_order_result()
# sdk.modify_price(orderResult[0], 26.80)
# print(orderResult[1])


@sdk.on('order')
def on_order(data):
    print(data)

@sdk.on('dealt')
def on_dealt(data):
    print(data)


@sdk.on('error')
def on_error(err):
    print(err)

# sdk.connect_websocket()

# order = OrderObject(999999)
# print(order.buySell)


# test_obj(order)

# sdk = CoreSDK()
# print(sdk.access_token)
# sdk.login("88400560553", "12345678")
# print(sdk.access_token)
# print(sdk.access_token[0:10])
# print(sdk.get_order_result("FUGLE12345678", "7317257e8d72ce8a2957987b53d12e7c430d3b79d35ac6b4be9e715e6d0a1090"))

#print(login("24550172", "12345678"))


#print(res)
