# Description: Iterative and Recursive functions that return the shortest and longest strings
# Name: Cupic, Aleksej
# Date: 11.18.19

def itershortestLongest(L):
    max_len=[]
    for i in range(0,len(L)):
        max_len.append(len(L[i]))
    long=max(max_len)
    short=min(max_len)
    shortlong=[]
    for j in range(0,len(L)):
        if len(L[j])==short:
            shortlong.append(L[j])
    for k in range(0,len(L)):
        if len(L[k])==long:
            shortlong.append(L[k])
    print(shortlong)
    return

def recurshortestLongest(L):
        return 0

string=input('Enter a list separeted by commas')
L=string.split(',')
itershortestLongest(L)
recurshortestLongest(L)



