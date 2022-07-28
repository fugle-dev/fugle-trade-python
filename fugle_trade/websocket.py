"""
handle websocket connection and callback registration
"""

import json
from websocket import WebSocketApp
from fugle_trade_core.fugle_trade_core import convert_ws_object

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
        """callback function for websocket message, pipe to order or dealt
        based on message type"""
        try:
            data = json.loads(convert_ws_object(in_message))
            if data['kind'] == "ACK":
                self.on_order(data)

            if data['kind'] == "MAT":
                self.on_dealt(data)
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
