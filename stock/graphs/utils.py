import tkinter as tk
from tkinter import ttk
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import sys
import requests
sys.path.append('../')
from swyftx import SWYFTX

class RealtimeLineGraphMeter:
    def __init__(self, root, max_data_points=100, y_label="BTC Price", meter_range=(59500, 60500)):
        self.root = root
        self.max_data_points = max_data_points
        self.data = deque(maxlen=max_data_points)  # Circular buffer for data points
        self.y_label = y_label
        self.meter_range = meter_range  # Range for meter visualization
        self.running = True # Flag to indicate if the animation is running
        self.animation_id = None

        self.fig, (self.ax_line, self.ax_meter) = plt.subplots(1, 2, figsize=(10, 5))

        # Line graph setup
        self.line, = self.ax_line.plot([], [], label=y_label)
        self.ax_line.set_xlabel("Time")
        self.ax_line.set_ylabel(y_label)
        self.ax_line.set_ylim(self.meter_range)  # Match meter range for visual consistency

        # Meter setup (using Matplotlib patches for customization)
        self.meter_patch = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='lightblue')
        self.meter_fill = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='green')
        self.ax_meter.add_patch(self.meter_patch)
        self.ax_meter.add_patch(self.meter_fill)
        self.ax_meter.set_aspect('equal')  # Ensure square aspect ratio
        self.ax_meter.set_xlim(0, 1)
        self.ax_meter.set_ylim(0, 1)
        self.ax_meter.set_xticks([])  # Hide x-axis ticks
        self.ax_meter.set_yticks([])  # Hide y-axis ticks

        plt.tight_layout()

        # Tkinter Canvas for Matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Initial data
        self.update(random.uniform(self.meter_range[0], self.meter_range[1]))
        
        # Start the animation
        self.scheduled_animation()

        # bind graceful exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update(self, new_data):
        self.data.append(new_data)

        # Update line graph
        self.line.set_data(range(len(self.data)), self.data)
        self.ax_line.set_xlim(0, self.max_data_points)  # Adjust x-axis for scrolling effect

        # update y-axis limits
        min_data = min(self.data) if self.data else self.meter_range[0]
        max_data = max(self.data) if self.data else self.meter_range[1]
        self.ax_line.set_ylim(min_data, max_data)

        # Update meter visualization
        meter_value = (new_data - self.meter_range[0]) / (self.meter_range[1] - self.meter_range[0])
        meter_value = min(max(meter_value, 0), 1)  # Clamp meter value to range
        self.meter_fill.set_height(meter_value)

        # Redraw the plot efficiently
        self.canvas.draw()

    def animate(self):
        if not self.running:
            return

        # Simulate new data point (replace with actual data fetching logic)
        new_data = random.uniform(self.meter_range[0], self.meter_range[1])
        # TODO: change data source
        # new_data = float(SWYFTXobj.get_btc_price())
        # new_data = float(BINANCEdata())

        self.update(new_data)
        
        # Schedule the next update
        self.scheduled_animation()
    
    # Scheduled animation
    def scheduled_animation(self):
        self.animation_id = self.root.after(1000, self.animate) # called after 1000ms
    
    def on_close(self):
        self.running = False
        if self.animation_id:
            self.root.after_cancel(self.animation_id) # Cancel the scheduled animate callbacks

        # clean up
        self.root.destroy()
        sys.exit()

def BINANCEdata():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()['price']


if __name__ == "__main__":
    # SWYFTXobj = SWYFTX()
    # print(SWYFTXobj.get_headers())
    root = tk.Tk()
    root.title("Real-Time Line Graph Meter")

    app = RealtimeLineGraphMeter(root)

    root.mainloop()