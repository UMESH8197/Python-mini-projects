# Price Elasticity of Demand using Python
# it means the degree to which the demand for a product changes with an increase or decrease in its price. 
# For example, the demand for a product increases by 20% due to a 10% decrease in its price. 
# This is what it means to change in demand with the change in the price of a product. And 
# when you calculate the degree to which demand changes, it’s called the price elasticity of demand. 

# To calculate the price elasticity of demand, you have to use the formula mentioned below:

# Percentage Change in Quantity Demanded / Percentage Change in the Price

import pandas as pd
data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35], 
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()
data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
print(data)