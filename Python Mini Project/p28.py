# Index of Maximum Value in a Python List

def maximum(x):
    maximum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[maximum_index]:
            maximum_index = current_index
        current_index = current_index + 1
    return maximum_index
a = [23,78,45,20,70,65,111,15,54]
print(maximum(a))

