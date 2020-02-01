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


# To create the 9*9
# below is the exercise answer:
#https://github.com/cancan-huang/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md

for i in range(0,10):
    for j in range(1, i + 1):
        results = i * j
        print(str(i),'*',str(j),'=',str(results),end = '\t')
# to separate different lines
    print()

'''

# My own code
for i in range(0,10):
    # this code should be improve because we do not need to show the duplicates
    for j in range(1, 10):
        results = i * j
        print(str(i),'*',str(j),'=',str(results),end = ' ')
# to separate different lines
    print()
'''

# practice print the pattern

for i in range(1,6):
    print("*" * i,end = ' ')
    print()


for i in range(1,6):
    print(' ' * (5 - i ), "*" * i, end = ' ' )
    print()

for i in range(1,6):
    print(' ' * int( ( 10 - 2 * i ) /2 ), '*' * int( 2 * i - 1 ), ' ' *  int(( 10 - 2 * i ) /2 ))
