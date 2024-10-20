# Description: a program that creates, sorts, and searches for numbers in a list
# Name: Cupic, Aleksej
# Date: 10.30.19

import random

def sort(num): # selection sort code from lecture
    for i in range(0,len(num)-1):
        minVal=num[i]
        minIndex=i
        for j in range(i+1,len(num)):
            if num[j]<minVal:
                minVal=num[j]
                minIndex=j
        num[minIndex]=num[i]
        num[i]=minVal
    return num

def binsearch(num,target):
    first=0
    last=len(num)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if num[mid]==target:
            found=True
        else:
            if target<num[mid]:
                last=mid-1
            else:
                first=mid+1
    return found


# main
num=[]
for i in range(10):
    number=random.randint(0,99)
    while number in num:
        number=random.randint(0,99)
    num.append(number)
print('List of numbers: ',num)
print('List of numbers sorted: ',sort(num))
hit=0
count=0
while hit==0:
    target=random.randint(0,99)
    print('Target = ',target)
    if binsearch(num,target)==True:
        hit=1
    count+=1
print('Count = ',count)


        
    
