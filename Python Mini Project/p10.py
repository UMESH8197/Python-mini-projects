# Visualize Linear Relationship using Python
# When the value of variable increases or decreases with the increase or decrease in the value of another variable, 
# then it is nothing but a linear relationship. When we visualize a linear relationship, 
# it shows whether the relationship between the two features is linear or not.

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()

figure = px.scatter(data_frame=data, x= 'Impressions', y= 'Likes', size= 'Likes', trendline= 'ols', title= 'Relationships Between Likes and Impressions' )
print(figure.show())

# To visualize linear relationships using matplotlib, you have to use seaborn.regplot method.

plt.figure(figsize= (10,8))
plt.style.use('fivethirtyeight')
plt.title('Relationships Between Likes and Impressions')
sns.regplot(x='Impressions', y='Likes',data=data)
# print(plt.show())

