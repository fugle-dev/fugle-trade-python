import pytest
from configparser import ConfigParser
from fugle_trade.sdk import SDK

@pytest.fixture(scope='session')
def sdk():
    config = ConfigParser()
    config.read('./tests/config.txt')
    sdk = SDK(config)
    return sdk
