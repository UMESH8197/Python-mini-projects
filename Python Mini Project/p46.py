# Pearson Correlation using Python
# When two or more features are related to each other in such a way that if the value of 1 features increases, 
# the value of the other feature also increases or decreases. This is what correlation means.

# What is Correlation?
# Correlation means finding the relationship between variables. In data science, we use correlation to find features 
# that are positively and negatively correlated with each other so that we can choose the best features to train a machine learning model.

# The degree of correlation is between -1 and 1. When the value of the correlation between the features is 1, then 
# those features are positively correlated with each other, and when the value of the correlation between the features 
# is -1, it means that those features are negatively correlated to each other.
# When the value of the correlation between the features is equal to 0, we can say that there is no correlation 
# between the features. In machine learning, we can use correlation to check the relationship between all the features 
# regarding the target label. So we can select those features to train the machine learning model which are highly 
# correlated to the target label

# Pearson Correlation Formula: 

# Pearson Correlation coefficient Formula
# r	correlation coefficient
# x_{i}	values of the x-variable in a sample
# \bar{x}	mean of the values of the x-variable
# y_{i}	values of the y-variable in a sample
# \bar{y}	mean of the values of the y-variable

# Pearson correlation is a statistical technique for measuring the degree of the linear relationship between two or more 
# features. Demand and supply are the best examples of understanding of Pearson’s correlation. For example, 
# the supply of a product will increase when the demand for the product increases, and 
# the supply of the product will decrease when the demand for that product increases.

# Positive values signify a positive linear correlation.
# Negative values mean negative linear correlation.
# 0 means no linear correlation.
# The closer the value is to 1 or -1, the stronger the linear correlation.


import pandas as pd
movies = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace=True, axis=1)
correlations = movies.corr(method='pearson')
# Correlation Between All The Features
print(correlations)

# Correlation Between A Particular column "Year"
print(correlations["Year"])

# Visualizing Correlation
import seaborn as sns

import matplotlib.pyplot as plt
sns.heatmap(correlations)
plt.show()