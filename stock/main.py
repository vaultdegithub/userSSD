
from utils import generate_prices, visualize_prices, calculate_rsi, line_plot, calculate_volatility
from utils import testBinanceSpotLib, testPythonBinance
import numpy as np

def main():
    # prices_df = generate_prices(60, volatility=0.02)
    # print(calculate_volatility(prices_df["Close"]))

    # rsi_values = calculate_rsi(prices_df["Close"], period=14)
    # rsi_print = np.pad(rsi_values, (13,0), 'constant', constant_values=0)
    # # line_plot(prices_df.index, prices_df["Close"], rsi_print, label1="Close Price", label2="RSI")

    # # line_plot(prices_df)

    testBinanceSpotLib()
    testPythonBinance()


if __name__ == '__main__':
    main()

