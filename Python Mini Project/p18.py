# Remove Cuss Words using Python
from better_profanity import profanity
word = "please leave me alone i am just piss off"
censored = profanity.censor(word)
print(censored)