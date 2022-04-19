"""
handle websocket connection and callback registration
"""

import json
import re
from websocket import WebSocketApp

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

class WebsocketHandler():
    """Handle Websocket connection"""
    def __init__(self):
        self.__ws = None
        default_fun = lambda x: print("in default function")
        self.on_order = default_fun
        self.on_dealt = default_fun
        self.on_error = default_fun
        self.on_close = default_fun

    def ws_on_message(self, _, in_message):
        """callback function for websocket message, pipe to order or dealt based on message type"""
        message = json.loads(in_message)
        # if message['data']['$type'] == "System.String" :
        #     return
        try:
            data = json.loads(message['data']['$value'])
            if data['Kind'] == "ACK":
                self.on_order(convert_to_snakecase(data))

            if data['Kind'] == "MAT":
                self.on_dealt(convert_to_snakecase(data))
        except:
            pass

    def ws_on_error(self, _, error):
        """callback function for websocket error"""
        self.on_error(error)

    def ws_on_close(self, _, error):
        """callback function for websocket close"""
        self.on_close(error)

    def set_callback(self, name, func):
        """for upper scope to set different types of callback function"""
        allowed_callback = ['order', 'dealt', 'error', 'close']
        if name in allowed_callback:
            setattr(self, "on_" + name, func)
        else:
            raise Exception("callback " + name + " not allowed")

    def connect_websocket(self, urlEntry):
        """start to connect websocket"""
        self.__ws = WebSocketApp(
            urlEntry,
            on_message=self.ws_on_message,
            on_error=self.ws_on_error,
            on_close=self.ws_on_close
        )
        self.__ws.run_forever()
