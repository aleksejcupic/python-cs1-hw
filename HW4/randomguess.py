# description: a game that has the user guess a randomly generated number with no repeats
# name: Cupic, Aleksej
# date: 9.26.19

import random

# function to get a random number with no repeats
def getRandom():
    number=str(random.randint(0,9))
    while len(number)<4:
        number2=str(random.randint(0,9))
        for i in range(len(number)):
            if number[i]==number2:
                number2=str(random.randint(0,9))
        number=number+number2
    return number
        
# main

# description of game
print('Guess the 4-digit random nonnegative integer - no repeats')
print('As the program proceeds, the computer will tell you if')
print('a digit appears in the number, and if it is in the correct position')
print('Good Luck!')

target=str(getRandom())
guess=str(input('Enter a 4-digit number with no repeats: '))
hits=0
guesscount=0

# checking the guess
while hits<4:
    hits=0
    if guesscount==0:
        guesscount=guesscount+1
        for j in range(4):
            if guess[j] in target:
                print('Yes ',guess[j],' is present')
                if guess[j]==target[j]:
                    print('and in the correct position')
                    hits=hits+1
            else:
                print(guess[j],' is not present')
    else:
        guess=str(input('Enter another number: '))
        for j in range(4):
            if guess[j] in target:
                print('Yes ',guess[j],' is present')
                if guess[j]==target[j]:
                    print('and in the correct position')
                    hits=hits+1
            else:
                print(guess[j],' is not present')
print('WINNER!')

# end
