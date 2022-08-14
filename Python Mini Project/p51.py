# Get Stock Price Data using Python

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


# The above code will collect the stock price data from today to the last 360 days. In this dataset, Date is not a column,
# it’s the index of this dataset. To use this data for any data science task, we need to convert this index into 
# a column. Below is how you can do that:

data['Date'] = data.index
data = data[['Date','Open','High','Low','Close','Adj Close','Volume']]
data.reset_index(drop=True,inplace=True)
print(data.head())

# data["Date"] = data.index
# data = data[["Date", "Open", "High", 
#              "Low", "Close", "Adj Close", "Volume"]]
# data.reset_index(drop=True, inplace=True)
# print(data.head())