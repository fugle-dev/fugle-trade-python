import pytest
from fugle_trade.order import OrderObject
from fugle_trade.constant import (
    Action,
    APCode
)


def test_machine_time(sdk):
    result = sdk.get_machine_time()
    assert result['time'] == "2022-03-10 10:23:48.464"


def test_place_order_login_first(sdk):
    with pytest.raises(Exception, match='Must login first'):
        order = OrderObject(
            Action.Buy,
            7.64,
            "2888",
            1,
            APCode.Common
        )
        sdk.place_order(order)


def test_place_order(sdk):
    sdk.login()
    order = OrderObject(
        Action.Buy,
        7.64,
        "2888",
        1,
        APCode.Common
    )
    result = sdk.place_order(order)
    assert result['ord_no'] == "A7321"
    assert result['ret_code'] == "000000"
    assert result['ret_msg'] == ""


def test_get_key_info(sdk):
    result = sdk.get_key_info()
    assert result['api_key'] == "XXXXXXXXXXXXXXXX"
    assert result['scope'] == "C"


def test_get_order_results(sdk):
    result = sdk.get_order_results()
    assert result[0]['ord_no'] == ""
    assert result[0]['pre_ord_no'] == "P0D832B7"
    assert result[0]['stock_no'] == "2884"
    assert result[0]['od_price'] == 25.0
    assert result[0]['avg_price'] == 0.0

    assert result[1]['ord_no'] == "B9999"
    assert result[1]['pre_ord_no'] == ""
    assert result[1]['stock_no'] == "0050"
    assert result[1]['od_price'] == 140.0
    assert result[1]['avg_price'] == 0.0


def test_get_inventories(sdk):
    result = sdk.get_inventories()
    assert result[0]['stk_no'] == "0056"
    assert result[0]['stk_na'] == "元大高股息"
    assert result[0]['price_mkt'] == "33.49"


def test_get_settlements(sdk):
    result = sdk.get_settlements()
    assert result[0]['date'] == "20220222"
    assert result[0]['c_date'] == "20220224"
    assert result[0]['price'] == "-30042"


def test_get_transactions(sdk):
    result = sdk.get_transactions('1m')
    assert result[0]['stk_no'] == "2884"
    assert result[0]['buy_sell'] == "B"
    assert result[0]['qty'] == "1000"
