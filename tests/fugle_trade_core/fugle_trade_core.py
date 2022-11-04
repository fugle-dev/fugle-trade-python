import os
import re
import json

JSON_ROOT = os.path.realpath(os.path.dirname(__file__)) + '/fixtures'

def convert_ws_object(in_message):
    message = json.loads(in_message)
    data = json.loads(message['data']['$value'])
    return convert_to_snakecase(data)

def convert_to_snakecase(original_dict):
    transformed_dict = {}
    array_items = []
    if not isinstance(original_dict, list):
        for k in original_dict.keys():
            value = re.sub(r'(?<!^)(?=[A-Z])', '_', k).lower()
            if not isinstance(original_dict[k], list):
                if isinstance(original_dict[k], dict):
                    transformed_dict[value] = convert_to_snakecase(original_dict[k])
                else:

                    transformed_dict[value] = original_dict[k]
            else:

                array_items = []
                for i in range(len(original_dict[k])):
                    if isinstance(original_dict[k][i], dict):
                        array_items.append(convert_to_snakecase(original_dict[k][i]))
                        transformed_dict[value] = array_items
                    else:
                        transformed_dict[value] = original_dict[k]
    else:
        array_items = []
        for item in original_dict:
            array_items.append(convert_to_snakecase(item))
        transformed_dict.update(array_items)
    return transformed_dict


def load_json(filename):
    return json.dumps(load_json_dic(filename))

def load_json_dic(filename):
    json_url = os.path.join(JSON_ROOT, filename)
    raw_content = json.load(open(json_url))
    content = convert_to_snakecase(raw_content)
    return content

class CoreSDK():
    def __init__(self, entry, account, cert_path, cert_pass, api_key, api_secret):
        self.isLogin = False

    def get_machine_time(self):
        return load_json("response-machine-time.txt")

    def get_key_info(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-key-info.txt")


    def get_inventories(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-inventories.txt")

    def get_order_results(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-orders.txt")

    def order(self, order):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-place-order.txt")

    def get_settlements(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-settlements.txt")

    def get_transactions(self, period):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-transactions.txt")

    def login(self, account, password):
        self.isLogin = True
        return load_json("response-login.txt")

    def get_volume_per_unit(self, stock_no):
        if not self.isLogin:
            raise TypeError("Must login first")
        return 1000

    def get_volume_per_unit(self, stock_no):
        if not self.isLogin:
            raise TypeError("Must login first")
        return 1000

    def get_balance(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-balance.txt")

    def get_trade_status(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-trade-status.txt")

    def get_market_status(self):
        if not self.isLogin:
            raise TypeError("Must login first")
        return load_json("response-market-status.txt")

    def modify_volume(self, order_result, cel_qty):
        if not self.isLogin:
            raise TypeError("Must login first")
        result = load_json_dic("response-modify.txt")
        result['data']['_input'] = {}
        result['data']['_input']['order_result'] = order_result
        result['data']['_input']['cel_qty'] = cel_qty
        return json.dumps(result)
