import requests
import sys
sys.path.append('../')
from swyftx import SWYFTX
from algo import MovingAverageCrossover, ExponentialMovingAverageCrossover
def BINANCEdata():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()['price']


while True:
    prices = None
    mac = MovingAverageCrossover(short_window=3, long_window=5)
    mac.generate_signals(prices)
    signals = mac.get_signals()
    if signals["short_mavg"].iloc[-1] > signals["long_mavg"].iloc[-1]:
        print("Buy")
    elif signals["short_mavg"].iloc[-1] > signals["price"].iloc[-1]:
        print("Sell")
    