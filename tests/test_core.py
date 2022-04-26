# content of test_class_demo.py
import pytest
from configparser import ConfigParser
from fugle_trade.sdk import SDK


class TestSDKInitialInstance:
    def test_empty_config_file(self):
        config = ConfigParser()
        with pytest.raises(Exception):
            sdk = SDK(config)


    def test_core_empty_section(self):
        config = ConfigParser()
        config['Core'] = {}
        config['Cert'] = {}
        config['Api'] = {}
        config['User'] = {}
        with pytest.raises(Exception, match='please give Core Entry value'):
            SDK(config)


    def test_cert_empty_section(self):
        config = ConfigParser()
        config['Core'] = { 'Entry' : 'xxx' }
        config['Cert'] = {}
        config['Api'] = {}
        config['User'] = {}
        with pytest.raises(Exception, match='please give correct Cert Path'):
            sdk = SDK(config)

    def test_cert_path_wrong_format(self):
        config = ConfigParser()
        config['Core'] = { 'Entry' : 'xxx' }
        config['Cert'] = { 'Path': '123' }
        config['Api'] = {}
        config['User'] = {}
        with pytest.raises(Exception, match='please give correct Cert Path'):
            sdk = SDK(config)

    def test_api_empty_section(self):
        config = ConfigParser()
        config['Core'] = { 'Entry' : 'xxx' }
        config['Cert'] = { 'Path': 'xxx.p12' }
        config['Api'] = {}
        config['User'] = {}
        with pytest.raises(Exception, match='please give correct Api Key and Secret'):
            sdk = SDK(config)

    def test_api_not_complete(self):
        config = ConfigParser()
        config['Core'] = { 'Entry' : 'xxx' }
        config['Cert'] = { 'Path': 'xxx.p12' }
        config['Api'] = { 'Key' : 'xxx'}
        config['User'] = {}
        with pytest.raises(Exception, match='please give correct Api Key and Secret'):
            sdk = SDK(config)

    def test_user_empty_section(self):
        config = ConfigParser()
        config['Core'] = { 'Entry' : 'xxx' }
        config['Cert'] = { 'Path': 'xxx.p12' }
        config['Api'] = { 'Key' : 'xxx', 'Secret': 'xxx'}
        config['User'] = {}
        with pytest.raises(Exception, match='please give correct User Account'):
            sdk = SDK(config)
