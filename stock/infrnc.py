from utils import DataCollector
from graphs import RealtimeLineGraphMeter

import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Real-Time Line Graph Meter")
    app = RealtimeLineGraphMeter(root)
    root.mainloop()

