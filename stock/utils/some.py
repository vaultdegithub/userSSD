import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import random

def line_plot(index, line1, line2=None, label1="Close Price", label2="RSI"):
  plt.plot(index, line1, label=label1, color='blue', linewidth=2)
  if line2 is not None:
    plt.plot(index, line2, label=label2, color='green', linewidth=1)
  
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.title('Line Plot')
  plt.legend()
  
  plt.grid(True)
  plt.show()


def visualize_prices(prices_df, title="Stock Prices"):
  fig, ax1 = plt.subplots(1, 1, figsize=(12, 6), sharex=True)

  # Line plot
  ax1.plot(prices_df.index, prices_df['Close'], label='Close Price')
  ax1.set_title('Line Plot')
  ax1.grid(True)
  ax1.legend()
  plt.suptitle(title)
  plt.show()


def calculate_rsi(prices, period=14):
  """
  This function calculates the RSI for a given list of prices and period.

  Args:
      prices: A list of historical closing prices.
      period: The number of periods to consider for the calculation.

  Returns:
      A list of RSI values for each price in the input list.
  """
  rsi_values = []
  avg_gain = 0
  avg_loss = 0

  for i in range(period):
    if i == 0:
      # Skip the first period as we don't have enough data for averages
      continue
    price_change = prices.iloc[i] - prices.iloc[i-1]
    if price_change > 0:
      avg_gain += price_change
    else:
      avg_loss += abs(price_change)  # Use absolute value for losses

  # Calculate initial RSI for period
  if avg_loss == 0:  # Avoid division by zero
    rs = 1.0
  else:
    rs = avg_gain / avg_loss
  rsi_values.append(100 - (100 / (1 + rs)))

  # Calculate RSI for subsequent periods using previous values
  for i in range(period, len(prices)):
    price_change = prices.iloc[i] - prices.iloc[i-1]
    if price_change > 0:
      avg_gain = (avg_gain * (period - 1) + price_change) / period
    else:
      avg_loss = (avg_loss * (period - 1) + abs(price_change)) / period
    rs = avg_gain / avg_loss
    rsi_values.append(100 - (100 / (1 + rs)))

  return rsi_values

def generate_prices(num_days, volatility=0.01):
  """
  This function generates a list of simulated historical closing prices for a stock.

  Args:
      num_days: The number of days to simulate.
      volatility: A factor controlling the price fluctuations (higher volatility leads to larger swings).

  Returns:
      A Pandas DataFrame with columns 'Date' and 'Close'.
  """
  prices = []
  opening_price = 100.0  # Starting price

  for i in range(num_days):
    price_change = random.uniform(-volatility, volatility) * opening_price
    closing_price = opening_price + price_change
    prices.append(closing_price)
    opening_price = closing_price

  # Create a Pandas DataFrame with dates as index
  dates = pd.date_range(start="2024-01-01", periods=num_days)
  df = pd.DataFrame({'Close': prices}, index=dates)

  return df

def calculate_volatility(prices):
  """
  This function calculates the volatility of a stock price series using standard deviation of daily returns.

  Args:
      prices: A list of numerical values representing historical closing prices.

  Returns:
      The standard deviation of daily price changes (volatility).
  """
  if len(prices) < 2:
    raise ValueError("At least two prices are required to calculate volatility.")

  # Calculate daily price changes (returns)
  daily_changes = np.diff(prices)

  # Calculate standard deviation of daily changes (volatility)
  volatility = np.std(daily_changes)

  return volatility
