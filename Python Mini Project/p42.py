# Plotting Annotations using Python
import matplotlib.pyplot as plt
x = [3, 5, 7, 8, 4]
y = [5, 3, 7, 8, 2]
plt.scatter(x, y)
plt.show()

# So as you can see we have plotted the figure without using annotations. Now let’s see how to annotate this graph 
# using Python to make it self-explanatory. I will represent the data points as the monthly outcomes:

import matplotlib.pyplot as plt
x = [3,5,7,8,4]
y = [5,3,7,8,2]
label = ['Jan','Feb','Mar','April','May']
plt.scatter(x,y)
for i, j in enumerate(label):
    plt.annotate(j,(x[i]+0.10, y[i]), fontsize=10)
plt.show()

