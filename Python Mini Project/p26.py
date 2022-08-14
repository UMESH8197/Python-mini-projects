# Python Program to Count Most Frequent Words in a File
words = []
with open(r"Use STAR Be the STAR.pdf","r") as f:
    for l in f:
        words.extend(l.split())
        
from collections import Counter
counts = Counter(words)
top = counts.most_common(5)
print(top)


