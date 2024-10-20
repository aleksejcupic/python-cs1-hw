import random

def mean(entry):
    num=0
    num2=0
    for i in range(0,len(entry)):
        num=num+int(entry[i])
        num2=num2+(int(entry[i])**2)
    mean=num/len(entry)
    return mean

def median(entry):
    sort=sortem(entry)
    length=len(sort)
    if length/2==length//2: # for even lists
        middle=length/2
        median1=sort[int(middle)-1]
        median2=sort[int(middle+1)-1]
        median=(int(median1)+int(median2))/2
    else: # for odd lists
        middle=length/2+1
        median=sort[int(middle)]
    return median

def mode(entry): # creates frequency list, finds largest, checks all values if equal to largest, then finds its index position
    freq=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(entry)):
        num=int(entry[i])
        freq[num-1]=int(freq[num-1])+1
    largest=-1
    for j in range(10):
        candidate=int(freq[j])
        if candidate>largest:
            largest=candidate
            mode=int(freq.index(largest))+1
    null=[]
    num=freq.index(largest)
    for k in range(10):
        if largest in freq:
            null.append(freq.index(largest))
            freq[freq.index(largest)]=0
        else:
            break
    mode=[]
    for n in range(len(null)):
        mode.append(null[n]+1)
    return mode

def std_dev(entry): # does not use mean
    sumentry=0
    sumentry2=0
    for i in range(0,len(entry)):
        sumentry+=int(entry[i])
        sumentry2+=(int(entry[i])**2)
    sd=(((sumentry2-((sumentry**2)/len(entry)))/(len(entry)-1))**0.5)
    return sd

def sortem(entry): # selection sort
    for j in range(0,len(entry)-1):
        minVal=entry[j]
        minIndex=j
        for k in range(j+1,len(entry)):
            if entry[k]<minVal:
                minVal=entry[k]
                minIndex=k
        entry[minIndex]=entry[j]
        entry[j]=minVal
    return entry

# main
numints=random.randint(20,30)
print('Input ',numints,' widget scores')
entry=input('Input widget scores separated by commas: ')
entry=entry.split(',')
print('The input: ',entry)
#print('The sorted list (selection sort) of values is: ',sortem(entry))
print('The mean for ',numints,' values is ',mean(entry))
print('The median for ',numints,' values is ',median(entry))
print('The mode(s) for ',numints,' values is ',mode(entry))
print('The standard deviation for ',numints,' values is ',std_dev(entry))
