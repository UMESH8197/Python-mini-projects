# Time Series Graph using Python
# A time-series graph is a line plot that displays trends or patterns over a dataset collected over an interval of time. 
# For example, when you visualize a line plot of the daily sales made by a business, 
# you are visualizing a time-series graph.

# A time-series graph is a line plot used to visualize time series data. Time-series data is the data collected over
# an interval of time. Some of the popular examples of time series data are stock price data, daily sales data, daily covid cases data,

# While visualizing a time-series graph, the time intervals lie on the x-axis, and the data points collected over those 
# time intervals lie on the y-axis. For example, while visualizing a time-series graph of stock price data, 
# the date column will lie on the x-axis, and the price column will lie on the y-axis.

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download("AAPL",start=start_date, end=end_date,progress=False)

import plotly.express as px 
figure = px.line(data, x=data.index, y='Close')
figure.show()


