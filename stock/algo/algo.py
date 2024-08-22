import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
class MovingAverageCrossover:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame()

    def generate_signals(self, prices):
        self.signals['price'] = prices
        self.signals['short_mavg'] = prices.rolling(window=self.short_window, min_periods=1, center=False).mean()
        self.signals['long_mavg'] = prices.rolling(window=self.long_window, min_periods=1, center=False).mean()
        
        # Create signals
        self.signals['signal'] = 0.0
        self.signals.loc[self.short_window:,'signal'] = np.where(self.signals['short_mavg'][self.short_window:] > self.signals['long_mavg'][self.short_window:], 1.0, 0.0)   
        
        # Generate trading orders
        self.signals['positions'] = self.signals['signal'].diff()

        # Calculate confidence score based on the distance between moving averages
        self.signals['score'] = abs(self.signals['short_mavg'] - self.signals['long_mavg']) / self.signals['long_mavg']
        self.signals['score'] = self.signals['score'].fillna(0).multiply(1000)

    def plot_signals(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plotting the closing price
        self.signals['price'].plot(ax=ax, color='r', lw=1., label='Price')
        
        # Plotting the short and long moving averages
        self.signals['short_mavg'].plot(ax=ax, color='g', lw=1., label='Short moving average')
        self.signals['long_mavg'].plot(ax=ax, color='b', lw=1., label='Long moving average')
        
        # Plotting buy signals with confidence score
        buys = self.signals[self.signals['positions'] == 1.0]
        ax.plot(buys.index,
                 self.signals['short_mavg'][self.signals['positions'] == 1.0],
                 '^', markersize=10, color='m', lw=0, label='Buy Signal')
        for i in buys.index:
            ax.annotate(f"{buys['score'][i]:.2f}", (i, buys['short_mavg'][i]), textcoords="offset points", xytext=(0, 10), ha='center') # type: ignore
        
        # Plotting sell signals with confidence score
        sells = self.signals[self.signals['positions'] == -1.0]
        ax.plot(sells.index,
                 self.signals['short_mavg'][self.signals['positions'] == -1.0],
                 'v', markersize=10, color='k', lw=0, label='Sell Signal')
        for i in sells.index:
            ax.annotate(f"{sells['score'][i]:.2f}", (i, sells['short_mavg'][i]), textcoords="offset points", xytext=(0, -15), ha='center') # type: ignore
        
        plt.title('Moving Average Crossover Strategy')
        plt.legend()
        plt.show()
    
    def get_signals(self):
        return self.signals

class ExponentialMovingAverageCrossover:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame()

    def generate_signals(self, prices):
        self.signals['price'] = prices
        self.signals['short_ema'] = prices.ewm(span=self.short_window, adjust=False).mean()
        self.signals['long_ema'] = prices.ewm(span=self.long_window, adjust=False).mean()
        
        # Create signals
        self.signals['signal'] = 0.0
        self.signals['signal'][self.short_window:] = np.where(
            self.signals['short_ema'][self.short_window:] > self.signals['long_ema'][self.short_window:], 1.0, 0.0)
        
        # Generate trading orders
        self.signals['positions'] = self.signals['signal'].diff()
        
        # Calculate confidence score based on the absolute difference
        self.signals['score'] = abs(self.signals['short_ema'] - self.signals['long_ema']).multiply(1e8)

    def plot_signals(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plotting the closing price
        self.signals['price'].plot(ax=ax, color='r', lw=1., label='Price')
        
        # Plotting the short and long moving averages
        self.signals['short_ema'].plot(ax=ax, color='g', lw=1., label='Short EMA')
        self.signals['long_ema'].plot(ax=ax, color='b', lw=1., label='Long EMA')
        
        # Plotting buy signals with confidence scores
        buys = self.signals[self.signals['positions'] == 1.0]
        ax.plot(buys.index, buys['short_ema'], '^', markersize=10, color='m', lw=0, label='Buy Signal')
        for i in buys.index:
            ax.annotate(f"{buys['score'][i]:.2f}", (i, buys['short_ema'][i]), textcoords="offset points", xytext=(0, 10), ha='center') # type: ignore
        
        # Plotting sell signals with confidence scores
        sells = self.signals[self.signals['positions'] == -1.0]
        ax.plot(sells.index, sells['short_ema'], 'v', markersize=10, color='k', lw=0, label='Sell Signal')
        for i in sells.index:
            ax.annotate(f"{sells['score'][i]:.2f}", (i, sells['short_ema'][i]), textcoords="offset points", xytext=(0, -15), ha='center') # type: ignore
        
        plt.title('Exponential Moving Average Crossover Strategy with Confidence Scores')
        plt.legend()
        plt.show()


class dynamic_mac:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame(columns=['price', 'short_mavg', 'long_mavg', 'signal', 'positions', 'score'])

    def generate_signals(self, new_prices):
        new_data = pd.DataFrame(new_prices, columns=['price'])
        self.signals = pd.concat([self.signals, new_data], ignore_index=True)
        self.signals['short_mavg'] = self.signals['price'].rolling(window=self.short_window, min_periods=1).mean()
        self.signals['long_mavg'] = self.signals['price'].rolling(window=self.long_window, min_periods=1).mean()
        
        # Create signals
        self.signals['signal'] = 0.0
        self.signals.loc[self.short_window:,'signal'] = np.where(self.signals['short_mavg'][self.short_window:] > self.signals['long_mavg'][self.short_window:], 1.0, 0.0)   
        
        # Generate trading orders
        self.signals['positions'] = self.signals['signal'].diff()

        # Calculate confidence score based on the distance between moving averages
        self.signals['score'] = abs(self.signals['short_mavg'] - self.signals['long_mavg']) / self.signals['long_mavg']
        self.signals['score'] = self.signals['score'].fillna(0).multiply(1000)

        return self.signals


        
    


