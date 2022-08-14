# Count Number of Words in a Column using Python
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')

data['NumberOfWords']= data['Article'].apply(lambda n:len(n.split()))
print(data.head())
