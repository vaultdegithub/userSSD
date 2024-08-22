import time
import requests
def BINANCEdata():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()['price']


for _ in range(10):
    print(BINANCEdata())
    time.sleep(1)