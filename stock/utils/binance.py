import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

binance_com = {
    "api": kXLzeKEKMF9udzqv66ZRqDGTLPYjQcGM74A6Fh7zdHRwEuA8pTPIMT7X5hWTTvE7,
    "api_secret": iIqrkwav3CcWX6uUpBMkhgeHpi6sXEbPfAc5tWklcsxlSL5Qef2e0uHAD7ojQtBE
    }

logging.basicConfig(level=logging.DEBUG, filename='sample.log')

def testBinanceSpotLib():
    spot_client = Client()
    
    logging.info(spot_client.exchange_info(symbol='BTCUSDT'))


def testPythonBinance():
    
    
    pass