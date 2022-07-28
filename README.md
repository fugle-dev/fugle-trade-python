# Fugle Trade Python SDK

## 事前準備

可以參考 https://developer.fugle.tw/docs/trading/prerequisites 完成申請金鑰相關步驟

## QuickStart

```python
from configparser import ConfigParser
from fugle_trade.sdk import SDK
from fugle_trade.order import OrderObject
from fugle_trade.constant import (APCode, Trade, PriceFlag, BSFlag, Action)

config = ConfigParser()
config.read('./config.ini')
sdk = SDK(config)
sdk.login()

order = OrderObject(
    buy_sell = Action.Buy,
    price = 28.00,
    stock_no = "2884",
    quantity = 2,
    ap_code = APCode.Common
)
sdk.place_order(order)

```

## Detail

所有 function 跟 response 可以在專屬文件頁查到相關資訊

https://developer.fugle.tw/docs/trading/reference/python


## License

[MIT](LICENSE)
