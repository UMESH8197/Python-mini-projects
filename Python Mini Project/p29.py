# Index of Minimum Value in a Python List


def minimum(x):
    minimum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] < x[minimum_index]:
            minimum_index = current_index
        current_index = current_index + 1
    return minimum_index
a = [22,44,55,33,11,66,77]
print(minimum(a))