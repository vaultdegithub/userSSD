import pandas as pd
import plotly.graph_objects as go

# Load the CSV file into a DataFrame
df = pd.read_csv('ohlcv.csv')
df = df.iloc[:, :-5]

# # Convert timestamp columns to datetime
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
df.iloc[:, -1] = pd.to_datetime(df.iloc[:, -1])
df = df.iloc[:100, :]

# # Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df.iloc[:,0],
                                     open=df.iloc[:,1],
                                     high=df.iloc[:,2],
                                     low=df.iloc[:,3],
                                     close=df.iloc[:,4],
                                     name='klines')])

# # Update layout for better visualization
fig.update_layout(title='Klines Candlestick Chart',
                  xaxis_title='Time',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)

# # Show the figure
fig.show()
