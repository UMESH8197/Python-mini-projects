# SequenceMatcher in Python
from difflib import SequenceMatcher
text1 = 'My name is Umesh Pawar'
text2 = 'Hi, My namw is Umesh Pawar'
sequenceScore = SequenceMatcher(None,text1,text2).ratio()
print("Both are {sequenceScore * 100} % similar")






# from difflib import SequenceMatcher
# text1 = "My Name is Aman Kharwal"
# text2 = "Hi, My Name is Aman Kharwal"
# sequenceScore = SequenceMatcher(None, text1, text2).ratio()
# print(f"Both are {sequenceScore * 100} % similar")