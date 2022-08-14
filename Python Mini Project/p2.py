# Find Missing Number using Python

def FindMissingNumber(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, length+1):
        if i not in numbers:
            output.append(i)
    return output
a = [1,2,3,4,6,8,9]
print(FindMissingNumber(a)) 
