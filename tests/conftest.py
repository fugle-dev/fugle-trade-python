import pytest
from configparser import ConfigParser
import sys
import os
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)+"/../"))
from fugle_trade.sdk import SDK

@pytest.fixture(scope='session')
def sdk():
    config = ConfigParser()
    config.read('./tests/config.txt')
    sdk = SDK(config)
    return sdk
