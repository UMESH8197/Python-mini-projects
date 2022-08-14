# Number Guessing Game using Python
import random
n = random.randrange(1,10)
guess = int(input('Enter a number: '))
while guess != n :
    if guess < n :
        print('Too low')
        guess = int(input('Enter Number Again: '))
    elif guess > n :
        print('Too High')
        guess = int(input('Enter Number Again: '))
    else :
        break
print('your guess is correct')
        