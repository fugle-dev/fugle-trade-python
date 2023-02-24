#from fugle_trade import sign_cert, login, get_order_result 

from configparser import ConfigParser
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

sdk = SDK(config)

import pprint
pp = pprint.PrettyPrinter(indent=2)
print(sdk.get_machine_time())
sdk.login()

order = OrderObject(
    Action.Buy,
    7.64,
    "2888",
    1,
    APCode.Common
)

# print(sdk.place_order(order))
# print(sdk.get_order_results())

# pp.pprint(sdk.get_transactions("1m"))

pp.pprint(sdk.get_transactions_by_date("2023-01-01", "2023-02-24"))
# InventoriesResult = sdk.get_inventories()

# pp.pprint(InventoriesResult)

# print(sdk.get_settlements())

# print(sdk.get_machine_time())
# orderResult = sdk.get_order_results()
# sdk.modify_volume(orderResult[0], celqty_share=2000)
# sdk.modify_price(orderResult[0], 10.5)
# print(orderResult[1])


@sdk.on('order')
def on_order(data):
    print(data)

@sdk.on('dealt')
def on_dealt(data):
    print(data)
# sdk.connect_websocket()
