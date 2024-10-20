# Description: Magic Square Program (without mod operator)
# Name: Cupic, Aleksej
# Date: 11.10.19

import random
#random.seed(0)

def printstatements():
    print('This program creates an odd-sided Magic Square,')
    print('where the sum of each row, column, and diagonal')
    print('adds up to the same number.')
    print()
    print('The program will also record and print the various')
    print('counts associated with specific moves during the')
    print('construction of the square.')
    print()
    print('Lastly, and only for the 3x3 Magic Square,')
    print('the program must count how many iterations it will')
    print('take to randomly create a square that is a perfect')
    print('duplicate of the 3x3 Magic Square.')
    print()
    
def magicsq(size):
    L=[]
    for row in range(size):
        L.append([])
    for i in range(size):
        for j in range(size):
            L[i].append(0)
    return L

def printHelper(magic_square,size):
    for i in range(0,size):
        print('\n')
        for j in range(0,size):
            print('\t',magic_square[i][j],end=' ')
    print()

def randomsquare(magic_square):
    magic_square=flat(magic_square)
    count=0
    target=False
    guess=[]
    while target==False:
        num=random.randint(1,9)
        if num not in guess:
            guess.append(num)
            for j in range(len(guess)):
                if guess[j]!=magic_square[j]:
                    guess=[]
                    count+=1
        if guess==magic_square:
            target=True
    print('It took ',count,' tries to get the Magic Square randomly.')

def fill(magic_square):
    col=size//2
    row=0
    magic_square[row][col]=1
    colout=0
    rowout=0
    block=0
    bothout=0
    incount=0
    for i in range(2,size**2+1):
        incounter=0
        col+=1
        row+=-1
        if col>size-1:
            col=0
            colout+=1
            incounter=1
        if row<0:
            row=size-1
            rowout+=1
            incounter=1
        if magic_square[row][col]==0:
            magic_square[row][col]=i
            if incounter==0:
                incount+=1
        else:
            block+=1
            row+=2
            col+=-1
            if col<0:
                col=size-1
                bothout+=1
            if row>size-1:
                row=1
            magic_square[row][col]=i
    summagic_square=magic_square[size//2][size//2]*size
    print()
    print('incount',incount)
    print('blocked',block)
    print('rowout',rowout)
    print('colout',colout)
    print('bothout',bothout)
    print()
    print('The sum of each row, column, and diagonal is: ',summagic_square)
    return magic_square
    
def flat(sq):
    if len(sq)==0:
        return []
    else:
        return sq[0]+flat(sq[1:])

def modfill(size):
    magic_square=[[0 for x in range(size)] for y in range(size)]
    row=0
    col=size//2
    magic_square[row][col]=1
    for num in range(2,size**2+1):
        col=(col+1)%size
        row=(row-1)%size
        if col>=0 and col<=size-1 and row>=0 and row<=size-1:
            if magic_square[row][col]==0:
                magic_square[row][col]=num
            else:
                row=(row+2)%size
                col=(col-1)%size
                magic_square[row][col]=num
    return magic_square
    
# main
printstatements()
size=int(input('Input size of an nxn odd-sided square: '))
magic_square=magicsq(size)
fill(magic_square)
printHelper(magic_square,size)
print()
print('The Magic Square using the Mod operator:')
print()
printHelper(modfill(size),size)

print()
if size==3: #creates the random magic square
    randomsquare(magic_square)

