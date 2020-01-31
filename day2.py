# Day 2
# practice while loop
# To guess the number
# code reference:
#https://github.com/cancan-huang/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md

import random as ran
answer = ran.randint(1,100)
times = 0

while True:
    times += 1
    guess = float(input('Plese enter the number you guess:'))
    if guess < answer:
        print('Your answer is smaller than the right answer. Try again!')
    elif guess > answer:
        print('Your answer is larger than the right answer. Try again!')
    else:
        print('You are right! You have tried '+str(times)+' times to get the right answer')
# one thing to notice is that the location of break, the break should below the else condition
# not the whole condition
        break

if times >= 10:
    print('Your chance runs out')
