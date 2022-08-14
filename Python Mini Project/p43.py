# Create Acronyms using Python

user_input = input("Enter a sentence : ")
text = user_input.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)

