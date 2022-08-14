# Python Program to Count Capital Letters in a File

with open("test5.txt") as f :
    count = 0
    text = f.read()
    for i in text:
        if i.isupper():
            count += 1
    print (count)



