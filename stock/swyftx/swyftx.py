SWYFTX_KEY = {
    "api": "kopwGy6-ChIjajv2__rUT46QEQ-KC8GNcyf1EoIjG74Y7",
    "api_secret": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJrVTRRelF6TlRaQk5rTkNORGsyTnpnME9EYzNOVEZGTWpaRE9USTRNalV6UXpVNE1UUkROUSJ9.eyJodHRwczovL3N3eWZ0eC5jb20uYXUvLWp0aSI6IjliNzRlMGEwLTQzNGUtNGM5My1hZjQzLTFmOGIzMjdiZGNhMyIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tbWZhX2VuYWJsZWQiOmZhbHNlLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLXVzZXJVdWlkIjoidXNyX1NuUTZTNXhEUmJGeHN3b1BMMzFQNjQiLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLWNvdW50cnlfbmFtZSI6IkF1c3RyYWxpYSIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tY2l0eV9uYW1lIjoiU3lkbmV5IiwiaXNzIjoiaHR0cHM6Ly9zd3lmdHguYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYyMzMyNjg5MGQzMTA5MDA2YTVlY2MwNyIsImF1ZCI6Imh0dHBzOi8vYXBpLnN3eWZ0eC5jb20uYXUvIiwiaWF0IjoxNzIxNzA1NTQ2LCJleHAiOjE3MjIzMTAzNDYsInNjb3BlIjoiYXBwLmFjY291bnQudGF4LXJlcG9ydCBhcHAuYWNjb3VudC5iYWxhbmNlIGFwcC5hY2NvdW50LnJlYWQgYXBwLnJlY3VycmluZy1vcmRlcnMucmVhZCBhcHAuYWRkcmVzcy5yZWFkIGFwcC5mdW5kcy5yZWFkIGFwcC5vcmRlcnMgYXBwLm9yZGVycy5jcmVhdGUgYXBwLm9yZGVycy5kZWxldGUgYXBwLm9yZGVycy5yZWFkIGFwcC5vcmRlcnMuZHVzdCBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIiwiYXpwIjoiRVF3M2ZhQXhPVGhSWVRaeXkxdWxaRGk4REhSQVlkRU8ifQ.neJx-ntgRhTkf8w355LzcRZT6UKe9OwpeoAe9q4cBJ1M0qFydaoY0IiI13BwTXMaEow_Nxusl93GdJ7sEIrUVMw997sk0kPFugniLIHYKpHdD0D3YBoT7o-IEVOpJ_FFbrpq47VeTr-3RhQgVC3Gp2iFsdSU9geOAokmxVDO9i6yfpYJRlNU7rUhu_gZSSJ3puhNsQbocS0tTFTIAimTBCptjJmJjxIIgu7yD2hhvT9s3-VB7arNzLTnImWSUEk6Jn_E2Y0EeRZNtSFvEJaV8pYB6bP6SFxmhEfH8e9kJ8WaFJ4VvnTuHudVX_PMZxur20Ylg5YPDD9XP70MiRChjw"
}

import requests
import random

class SWYFTX:
    def __init__(self):
        self.headers = self.generate_client_headers()
    
    def generate_client_headers(self):
        values = {
             "apiKey": SWYFTX_KEY["api"]
        }
        response = requests.post('https://api.swyftx.com.au/auth/refresh/', data=values)
        JWT = str(response.json()["accessToken"])

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + JWT,
            'User-Agent': 'MyApp/1.0'
        }
        return headers
    
    def get_headers(self):
        return self.headers
    
    # TODO: implement real BTC price
    def get_btc_price_buy(self):
        response = requests.get('https://api.swyftx.com.au/markets/info/basic/BTC/')
        return response.json()[0]['buy']
    
    def get_btc_price_sell(self):
        response = requests.get('https://api.swyftx.com.au/markets/info/basic/BTC/',)
        return response.json()[0]['sell']
    
    def get_profile(self):
        response = requests.get('https://api.swyftx.com.au/user/', headers=self.headers)
        return response.json()
    
    def view_price_alerts(self):
        response = requests.get('https://api.swyftx.com.au/alerts?primary=1&secondary=2&limit=10', headers=self.headers)
        return response.json()
    
    def get_account_balance(self):
        response = requests.get('https://api.swyftx.com.au/user/balance/', headers=self.headers)
        return response.json()
    
    def demo_account_balance(self):
        response = requests.get('https://api.demo.swyftx.com.au/user/balance/', headers=self.headers)
        return response.json()
    
    def demo_place_order(self):
        values = '''
        {
            "primary": "AUD",
            "secondary": "BTC",
            "quantity": "1000",
            "assetQuantity": "AUD",
            "orderType": 1
            }
        '''
        response = requests.post('https://api.demo.swyftx.com.au/orders/', data=values, headers=self.headers)
        return response.json()
    