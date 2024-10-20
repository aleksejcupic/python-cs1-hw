# Description: program that uses a file to find out ratings and price of restaurants in the Boston area
# Name: Cupic, Aleksej
# Date: 11.17.19

def cuisinehigh(rest2DList):
    med=[]
    sea=[]
    japan=[]
    ita=[]
    amer=[]
    sand=[]
    indi=[]
    kor=[]
    fre=[]
    for i in range(0,len(rest2DList)):
        if rest2DList[i][2]=='Mediterranean':
            med.append(i)
        elif rest2DList[i][2]=='Seafood':
            sea.append(i)
        elif rest2DList[i][2]=='Japanese':
            japan.append(i)
        elif rest2DList[i][2]=='Italian':
            ita.append(i)
        elif rest2DList[i][2]=='American':
            amer.append(i)
        elif rest2DList[i][2]=='Sandwiches':
            sand.append(i)
        elif rest2DList[i][2]=='Indian':
            indi.append(i)
        elif rest2DList[i][2]=='Korean':
            kor.append(i)
        elif rest2DList[i][2]=='French':
            fre.append(i)
    ratemed=0
    ratesea=0
    ratejapan=0
    rateita=0
    rateamer=0
    ratesand=0
    rateindi=0
    ratekor=0
    ratefre=0
    for j in range(0,len(med)):
        ratemed+=float(rest2DList[med[j]][4])
    for j in range(0,len(sea)):
        ratesea+=float(rest2DList[sea[j]][4])
    for j in range(0,len(japan)):
        ratejapan+=float(rest2DList[japan[j]][4])
    for j in range(0,len(ita)):
        rateita+=float(rest2DList[ita[j]][4])
    for j in range(0,len(amer)):
        rateamer+=float(rest2DList[amer[j]][4])
    for j in range(0,len(sand)):
        ratesand+=float(rest2DList[sand[j]][4])
    for j in range(0,len(indi)):
        rateindi+=float(rest2DList[indi[j]][4])
    for j in range(0,len(kor)):
        ratekor+=float(rest2DList[kor[j]][4])
    for j in range(0,len(fre)):
        ratefre+=float(rest2DList[fre[j]][4])
    ratemed=ratemed/len(med)
    ratesea=ratesea/len(sea)
    ratejapan=ratejapan/len(japan)
    rateita=rateita/len(ita)
    rateamer=rateamer/len(amer)
    ratesand=ratesand/len(sand)
    rateindi=rateindi/len(indi)
    ratekor=ratekor/len(kor)
    ratefre=ratefre/len(fre)
    highest=[ratemed,ratesea,ratejapan,rateita,rateamer,ratesand,rateindi,ratekor,ratefre]
    m=max(highest)
    if ratemed==m:
        highest='Mediterranean'
    elif ratesea==m:
        highest='Seafood'
    elif ratejapan==m:
        highest='Japanese'
    elif rateita==m:
        highest='Italian'
    elif rateamer==m:
        highest='American'
    elif ratesand==m:
        highest='Sandwiches'
    elif rateindi==m:
        highest='Indian'
    elif ratekor==m:
        highest='Korean'
    elif ratefre==m:
        highest='French'
    print('The cuisine with the highest rating is: ',highest,' with rating of: ',m)

def cuisinehigh2(rest2DList):
    names=[]
    for i in range(0,len(rest2DList)):
        if rest2DList[i][2] not in names:
            names.append(rest2DList[i][2])
    for j in range(0,len(rest2DList)):
        for k in range(0,len(names)):
            if rest2DList[j][2] in names[k]:
                names[k].append(rest2DList[j][4])
    print(names)
    names2=[]
    for l in range(0,len(names)):
        names2.append(names[l][0])
        names[l].pop(0)
    print(names)
    print(names2)

        
def cuisinelow(rest2DList):
    med=[]
    sea=[]
    japan=[]
    ita=[]
    amer=[]
    sand=[]
    indi=[]
    kor=[]
    fre=[]
    for i in range(0,len(rest2DList)):
        if rest2DList[i][2]=='Mediterranean':
            med.append(i)
        elif rest2DList[i][2]=='Seafood':
            sea.append(i)
        elif rest2DList[i][2]=='Japanese':
            japan.append(i)
        elif rest2DList[i][2]=='Italian':
            ita.append(i)
        elif rest2DList[i][2]=='American':
            amer.append(i)
        elif rest2DList[i][2]=='Sandwiches':
            sand.append(i)
        elif rest2DList[i][2]=='Indian':
            indi.append(i)
        elif rest2DList[i][2]=='Korean':
            kor.append(i)
        elif rest2DList[i][2]=='French':
            fre.append(i)
    ratemed=0
    ratesea=0
    ratejapan=0
    rateita=0
    rateamer=0
    ratesand=0
    rateindi=0
    ratekor=0
    ratefre=0
    for j in range(0,len(med)):
        ratemed+=float(rest2DList[med[j]][4])
    for j in range(0,len(sea)):
        ratesea+=float(rest2DList[sea[j]][4])
    for j in range(0,len(japan)):
        ratejapan+=float(rest2DList[japan[j]][4])
    for j in range(0,len(ita)):
        rateita+=float(rest2DList[ita[j]][4])
    for j in range(0,len(amer)):
        rateamer+=float(rest2DList[amer[j]][4])
    for j in range(0,len(sand)):
        ratesand+=float(rest2DList[sand[j]][4])
    for j in range(0,len(indi)):
        rateindi+=float(rest2DList[indi[j]][4])
    for j in range(0,len(kor)):
        ratekor+=float(rest2DList[kor[j]][4])
    for j in range(0,len(fre)):
        ratefre+=float(rest2DList[fre[j]][4])
    ratemed=ratemed/len(med)
    ratesea=ratesea/len(sea)
    ratejapan=ratejapan/len(japan)
    rateita=rateita/len(ita)
    rateamer=rateamer/len(amer)
    ratesand=ratesand/len(sand)
    rateindi=rateindi/len(indi)
    ratekor=ratekor/len(kor)
    ratefre=ratefre/len(fre)
    lowest=[ratemed,ratesea,ratejapan,rateita,rateamer,ratesand,rateindi,ratekor,ratefre]
    m=min(lowest)
    if ratemed==m:
        lowest='Mediterranean'
    elif ratesea==m:
        lowest='Seafood'
    elif ratejapan==m:
        lowest='Japanese'
    elif rateita==m:
        lowest='Italian'
    elif rateamer==m:
        lowest='American'
    elif ratesand==m:
        lowest='Sandwiches'
    elif rateindi==m:
        lowest='Indian'
    elif ratekor==m:
        lowest='Korean'
    elif ratefre==m:
        lowest='French'
    print('The cuisine with the lowest rating is: ',lowest,' with rating of: ',m)
    return

def resthigh(rest2DList):
    highest=[]
    for i in range(0,len(rest2DList)):
        highest.append(rest2DList[i][4])
    high=max(highest)
    highrate=[]
    for j in range(0,len(rest2DList)):
        if high==rest2DList[j][4]:
            highrate.append(rest2DList[j][0])
    print('The restaurant(s) with the highest rating is: ',highrate,' with a rating of: ',highest[-1])
    return

def restcost(rest2DList):
    cost=[]
    for i in range(0,len(rest2DList)):
        cost.append(len(rest2DList[i][3]))
    money=max(cost)
    highestcost=[]
    for j in range(0,len(rest2DList)):
        if money==len(rest2DList[j][3]):
            highestcost.append(rest2DList[j][0])
    print('The restaurant(s) with the highest cost is: ',highestcost)

def restbostlow(rest2DList):
    boston=[]
    for i in range(0,len(rest2DList)):
        if rest2DList[i][1]=='Boston':
            boston.append(rest2DList[i])
    rating=[]
    for j in range(0,len(boston)):
        rating.append(boston[j][4])
    low=min(rating)
    lowest=[]
    for k in range(0,len(rest2DList)):
        if low==rest2DList[k][4]:
            lowest.append(rest2DList[k][0])
    print('The restaurant in Boston with the lowest rating is: ',lowest)

        
# main
restFile=open('restaurants.HW9.txt','r')
linez=restFile.readlines()
print('\n Printed list line by line:')
print()
for r in linez:
    print(r)
print()
print('End of line by line print')
print()
rest2DList=[[s.lstrip().rstrip() for s in x.split(',')]
            for x in linez]
cuisinehigh(rest2DList)
cuisinelow(rest2DList)
resthigh(rest2DList)
restcost(rest2DList)
restbostlow(rest2DList)


