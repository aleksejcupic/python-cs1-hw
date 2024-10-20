# description: This program computes possible fines for motorists stopped on the Massachuesetts turnpike
# author: Cupic, Aleksej
# date: 09.14.2019

# function for fine 
def fine(speed,limit):
    if speed>limit:
        if speed>=(limit+10):
            mphover=speed-limit-10
            if mphover>=45:
                fine=500
            else:
                fine=mphover*10+50
        else:
            fine=50
    else:
        fine=0        
    return fine

# function for construction zone fine
def con_zone(fine):
    starttime=int(input('Enter Zone time begin in 24 hour format'))
    stoptime=int(input('Enter Zone time end in 24 hour format'))
    time=int(input('Enter stop time in 24 hour format'))
    stoptime2=stoptime+2400
    if starttime>stoptime:
        if time>=starttime and time+2400>stoptime2:
            con_fine=(fine)*3
        elif time<stoptime:
            con_fine=(fine)*3
        else:
            con_fine=(fine)*2
    elif starttime<stoptime:
        if time>starttime and time<stoptime:
            con_fine=(fine)*3
        else:
            con_fine=(fine)*2
    else:
        con_fine=(fine)*3
    return con_fine

# main section
print('This program computes possible fines for motorists stopped on the Massachusetts Turnpike')
speed=int(input('Enter speed in MPH:'))
limit=int(input('Enter speed limit in MPH:'))
if fine(speed,limit)>0:
    conzone=str(input('Is it a Construction Zone? Enter Y or N:'))
    if conzone.lower()=='y':
        print('The fine is $',con_zone(fine(speed,limit))+50,'including a $50 donation to the head injury fund')
    else:
        print('The fine is $',fine(speed,limit)+50,'including a $50 donation to the head injury fund')
else:
    print('No fine. Speed does not exceed Speed Limit')

# end
            
