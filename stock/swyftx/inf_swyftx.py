from swyftx import SWYFTX

SWYFTX = SWYFTX()

# print(SWYFTX.get_btc_price_buy())
# print(SWYFTX.get_btc_price_sell())
# print(SWYFTX.get_account_balance())
print(SWYFTX.demo_account_balance())
# print(SWYFTX.get_profile())
# print(SWYFTX.demo_place_order())



##############################################################################
# SWYFTX = {
#     "api": "zX3PXYmILvuLmxZWxC5vwXfhGzeHGUZu6DptJQsf80Luu",
#     "api_secret": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJrVTRRelF6TlRaQk5rTkNORGsyTnpnME9EYzNOVEZGTWpaRE9USTRNalV6UXpVNE1UUkROUSJ9.eyJodHRwczovL3N3eWZ0eC5jb20uYXUvLWp0aSI6IjZhODg4MTljLTNlMmItNDgyNC04OTA3LTg5YjI3MjA5M2Y0OSIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tbWZhX2VuYWJsZWQiOmZhbHNlLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLXVzZXJVdWlkIjoidXNyX1NuUTZTNXhEUmJGeHN3b1BMMzFQNjQiLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLWNvdW50cnlfbmFtZSI6IkF1c3RyYWxpYSIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tY2l0eV9uYW1lIjoiU3lkbmV5IiwiaXNzIjoiaHR0cHM6Ly9zd3lmdHguYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYyMzMyNjg5MGQzMTA5MDA2YTVlY2MwNyIsImF1ZCI6Imh0dHBzOi8vYXBpLnN3eWZ0eC5jb20uYXUvIiwiaWF0IjoxNzIwMzkyNzA4LCJleHAiOjE3MjA5OTc1MDgsInNjb3BlIjoiYXBwLmFjY291bnQudGF4LXJlcG9ydCBhcHAuYWNjb3VudC5iYWxhbmNlIGFwcC5hY2NvdW50LnJlYWQgYXBwLnJlY3VycmluZy1vcmRlcnMucmVhZCBhcHAuYWRkcmVzcy5yZWFkIGFwcC5mdW5kcy5yZWFkIGFwcC5vcmRlcnMucmVhZCBhcHAuYXBpLnJlYWQgb2ZmbGluZV9hY2Nlc3MiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6IkVRdzNmYUF4T1RoUllUWnl5MXVsWkRpOERIUkFZZEVPIn0.OdH-Dqz0_6OMzWAuPNTiEIv7OzdDecSB3k-4l-gl8P6APzcU7A1R1feBmvzsm9pIJEznnWx8KJd9X-CNZN_cMhKZ5fCAGwK_1PsJzLY3ghS8W6vsaFgzwhHUVcE6x4TIuy9fhQFRrXe2PXaIQq40751D9nNnmSf3sYmIlgoMpyWlk0hKNdVZrVPVJNiu6Lh49DDQqfSnR1pIEJJYgeyUCKFcMoGkuo9PbtrBCyWp8WzvfzHD-TDtEjqeP4-TM2FiFqoRLdOG77T16oTGlb6Pczixsczu1bKxwOhdFkyg6-jEYJneZuVNNkWCmD7mabuK7EbskiBjWTpELYfIHXNPUg"
# }
# import logging
# import requests
# import json

# values = {
#   "apiKey": SWYFTX["api"]
# }
# response = requests.post('https://api.swyftx.com.au/auth/refresh/', data=values)
# JWT = str(response.json()["accessToken"])

# headers = {
#   'Authorization': 'Bearer ' + JWT,
# }


# # response = requests.post('https://api.swyftx.com.au/auth/refresh/', data=values, headers=headers)
# # response = requests.get('https://api.swyftx.com.au/user/balance/', headers=headers)
# response = requests.get('https://api.swyftx.com.au/markets/info/basic/BTC/', headers=headers)
# # response = requests.get('https://api.swyftx.com.au/charts/v2/getLatestBar/AUD/BTC/ask/?resolution=1m', headers=headers)

# # TODO: read/create write log file 
# logging.basicConfig(level=logging.DEBUG, filename='swyftx.log')
# print(response.status_code)
# print(response.json()[0]['buy'])
# # print(response.json())
