BINANCE = {
    "api": "xyx",
    "api_secret": "xyz"
    }

from binance.spot import Spot as Client

# client = Client(base_url="https://api.binance.com")

# Initialize the client
client = Client(api_key=BINANCE['api'], api_secret=BINANCE['api_secret'])

try:
    # Attempt to get the account information to verify the keys
    account_info = client.account()
    print("API key and secret are valid.")
    print(account_info)
except Exception as e:
    print("Error: Invalid API key or secret.")
    print(e)
