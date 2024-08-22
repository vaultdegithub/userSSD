SWYFTX = {
    "api": "zX3PXYmILvuLmxZWxC5vwXfhGzeHGUZu6DptJQsf80Luu",
    "api_secret": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJrVTRRelF6TlRaQk5rTkNORGsyTnpnME9EYzNOVEZGTWpaRE9USTRNalV6UXpVNE1UUkROUSJ9.eyJodHRwczovL3N3eWZ0eC5jb20uYXUvLWp0aSI6IjZhODg4MTljLTNlMmItNDgyNC04OTA3LTg5YjI3MjA5M2Y0OSIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tbWZhX2VuYWJsZWQiOmZhbHNlLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLXVzZXJVdWlkIjoidXNyX1NuUTZTNXhEUmJGeHN3b1BMMzFQNjQiLCJodHRwczovL3N3eWZ0eC5jb20uYXUvLWNvdW50cnlfbmFtZSI6IkF1c3RyYWxpYSIsImh0dHBzOi8vc3d5ZnR4LmNvbS5hdS8tY2l0eV9uYW1lIjoiU3lkbmV5IiwiaXNzIjoiaHR0cHM6Ly9zd3lmdHguYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYyMzMyNjg5MGQzMTA5MDA2YTVlY2MwNyIsImF1ZCI6Imh0dHBzOi8vYXBpLnN3eWZ0eC5jb20uYXUvIiwiaWF0IjoxNzIwMzkyNzA4LCJleHAiOjE3MjA5OTc1MDgsInNjb3BlIjoiYXBwLmFjY291bnQudGF4LXJlcG9ydCBhcHAuYWNjb3VudC5iYWxhbmNlIGFwcC5hY2NvdW50LnJlYWQgYXBwLnJlY3VycmluZy1vcmRlcnMucmVhZCBhcHAuYWRkcmVzcy5yZWFkIGFwcC5mdW5kcy5yZWFkIGFwcC5vcmRlcnMucmVhZCBhcHAuYXBpLnJlYWQgb2ZmbGluZV9hY2Nlc3MiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6IkVRdzNmYUF4T1RoUllUWnl5MXVsWkRpOERIUkFZZEVPIn0.OdH-Dqz0_6OMzWAuPNTiEIv7OzdDecSB3k-4l-gl8P6APzcU7A1R1feBmvzsm9pIJEznnWx8KJd9X-CNZN_cMhKZ5fCAGwK_1PsJzLY3ghS8W6vsaFgzwhHUVcE6x4TIuy9fhQFRrXe2PXaIQq40751D9nNnmSf3sYmIlgoMpyWlk0hKNdVZrVPVJNiu6Lh49DDQqfSnR1pIEJJYgeyUCKFcMoGkuo9PbtrBCyWp8WzvfzHD-TDtEjqeP4-TM2FiFqoRLdOG77T16oTGlb6Pczixsczu1bKxwOhdFkyg6-jEYJneZuVNNkWCmD7mabuK7EbskiBjWTpELYfIHXNPUg"
}
from tkinter import messagebox
import requests
from datetime import datetime


# Function to fetch data from the API
def fetch_data(url, headers):
    try:
        response = requests.get(url=url, headers=headers)  # BTC
        data = str(response.json()[0]['buy'])
        return str("BUY_PRICE: " + str(datetime.now())+" ### " + data)
    except requests.RequestException as e:
        return {"error": str(e)}


# Function to be called when the button is clicked
def on_button_click():
    messagebox.showinfo("Message", "Hello, World!")