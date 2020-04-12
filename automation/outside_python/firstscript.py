#! python3
import sys
import random
import time

random.seed(time.time()) 
number = random.randint(1,20)
# print('Hello World!')
# print(sys.argv)
user_name = input('What is your name? ')
print('Hello {}, I am gussing number between 1 and 20. '.format(user_name))
count = 1

while True:
    guess = int(input('Guess a number: '))
    if count >= 10:
        print('Sorry you could not guess it in 10 rounds! you lost!')
        break
    if guess > number:
        print('You are guessing high!')
        count += 1
    elif guess < number:
        print('You are guessing low!')
        count += 1
    else:
        print('You guessed correct {} in {} guesses'.format(user_name,count))
        break