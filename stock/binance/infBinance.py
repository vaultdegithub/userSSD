BINANCE = {
    "api": "HiCvsxgq0Jj7TtppJ5f1l7wnBl8vE3b7BmBXYXnM0jl2O2ww5jQQmpEOpse6IoXt",
    "api_secret": "tlUXSEpEU9m9Hq2H9vcC78DmeN1qyaim1nupg75aJRedsCHlJMwie0SSAS98P6uI"
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