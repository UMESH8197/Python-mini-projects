# LCM using Python
# LCM stands for Least Common Multiple, which means finding the smallest number that is a multiple of two or more numbers


def least_common_multiple(a,b):
    if a > b :
        greater = a 
    elif b > a :
        greater = b 
    while(True):
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm 
print(least_common_multiple(10,12))
