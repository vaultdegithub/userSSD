from binance import Client
from datetime import datetime
KEY = {
    "api": "kXLzeKEKMF9udzqv66ZRqDGTLPYjQcGM74A6Fh7zdHRwEuA8pTPIMT7X5hWTTvE7",
    "api_secret": "iIqrkwav3CcWX6uUpBMkhgeHpi6sXEbPfAc5tWklcsxlSL5Qef2e0uHAD7ojQtBE"
    }

class API:
    def __init__(self):
        self.client = Client(api_key= KEY["api"], api_secret=KEY["api_secret"])
        # self.client = Client()

    def get_client(self):
        return self.client

    def get_server_time(self):
        return datetime.fromtimestamp(self.client.get_server_time()["serverTime"] / 1000)
    
    def get_ticker(self, symbol):
        return self.client.get_symbol_ticker(symbol=symbol)
    
    def get_orderbook_ticker(self, symbol):
        return self.client.get_orderbook_ticker(symbol=symbol)
    
    def get_client_info(self):
        return self.client.get_account()
    
    
def place_order(client, symbol, side=Client.SIDE_BUY, type=Client.ORDER_TYPE_MARKET, quantity=0.01):
    order = client.create_test_order(
        symbol=symbol,
        side=side,
        type=type,
        quantity=quantity
        )

    return order