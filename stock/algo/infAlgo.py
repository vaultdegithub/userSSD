import pandas as pd
import numpy as np
import random
from algo import MovingAverageCrossover, ExponentialMovingAverageCrossover

# prices = pd.Series([random.uniform(100, 200) for _ in range(10)])  # Your price data here
prices = pd.read_csv('ohlcv.csv', header=None).iloc[:100, 1]


# Example Usage: mac
# prices = pd.Series([0,1,2,3,4,5,6,7,8,9])  # Your price data here
mac = MovingAverageCrossover(short_window=3, long_window=5)
mac.generate_signals(prices)
print(mac.get_signals())
mac.plot_signals()

# TODO: dataStream = iterator(prices)
# for i in dataStream:
#     mac.generate_signals(i)
#     tkinter.update_plot(mac)