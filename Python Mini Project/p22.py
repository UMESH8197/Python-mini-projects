# Box Plot using Python
import pandas as pd
import plotly.express as px
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
# print(data.head())
fig = px.box(data, y='TV')
print(fig.show())



# import plotly.express as px
# fig = px.box(data, y="TV")
# fig.show()