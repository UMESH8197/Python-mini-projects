# Calculating Execution Time of a Python 
from time import time
start = time()

word = 'Full Stack Data Science'
text = word.split()
a = ''
for i in text :
    a = a + str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print('execution time is : ' , execution_time )

