# Mean Median and Mode using Python
l = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(l)/len(l)
print(mean)

# median 
l.sort()
if len(l) % 2 == 0:
    m1 = l[len(l)//2]
    m2 = l[len(l)//2-1]
    median = (m1+m2)/2
else:
    median = l[len(l)//2]
print(median)

# mode
frequency = {}
for i in l :
    frequency.setdefault(i,0)
    frequency[i] +=1
        
frequent = max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i
print(mode)

