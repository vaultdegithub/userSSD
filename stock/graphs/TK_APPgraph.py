import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import sys
sys.path.append('../')
from algo import dynamic_mac


import requests
def BINANCEdata():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()['price']

class TradingApp:
    def __init__(self, root, mac):
        self.root = root
        self.mac = mac

        #create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        #Create frame for the graph
        self.graph_frame = tk.Frame(self.main_frame)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        
        # Button to simulate incoming price data
        # self.update_button = tk.Button(root, text="Update Prices", command=self.update_prices)
        # self.update_button.pack()

        #Create frame for the result box
        self.result_frame = tk.Frame(self.main_frame, width=200)
        self.result_frame.pack(side=tk.BOTTOM, fill=tk.Y)

        #Add a label to display results
        self.result_label = tk.Label(self.result_frame, text="Results:", anchor="n")
        self.result_label.pack(fill=tk.BOTH, expand=1)


        # Placeholder for price data
        self.price_data = []

        self.scheduled_animation()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_prices(self):
        # Simulate new price data
        # new_price = self.price_data[-1] + np.random.randn() if self.price_data else 100
        new_price = float(BINANCEdata())
        self.price_data.append(new_price)

        # Generate signals with the new price data
        self.mac.generate_signals([new_price])

        # # Display current price in message box
    # messagebox.showinfo("Current Price", f"The current price is: {new_price}") #WILL OPEN DIALOG BOX

        # Update the plot
        self.plot_signals()

         # Update the result label
        latest_signal = self.mac.signals.iloc[-1] if not self.mac.signals.empty else None
        result_text = f"Latest Price: {new_price}\n"
        if latest_signal is not None:
            # result_text += f"Short MAVG: {latest_signal['short_mavg']}\n"
            # result_text += f"Long MAVG: {latest_signal['long_mavg']}\n"
            result_text += f"Signal: {latest_signal['signal']}\n"
            result_text += f"Score: {latest_signal['score']}"
        self.result_label.config(text=result_text)

        # Schedule the next update
        self.scheduled_animation()
    
    def scheduled_animation(self):
        self.animation_id = self.root.after(1000, self.update_prices) # called after 1000ms
    

    def plot_signals(self):
        self.ax.clear()
        self.mac.signals.plot(ax=self.ax, y=['price', 'short_mavg', 'long_mavg'], style=['b-', 'r-', 'g-'])
        self.canvas.draw()
    
    def on_close(self):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Moving Average Crossover Signals")

    short_window = 20
    long_window = 100
    mac = dynamic_mac(short_window, long_window)

    app = TradingApp(root, mac)
    root.mainloop()


