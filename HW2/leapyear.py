# description: Determine if a year is a leap year
# author: Cupic, Aleksej
# date: 9.10.2019

# user inputs a year
year=int(input('Enter a year:'))

# if statements to determine if the year is a leap year
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('This is a leap year')
        else:
            print('This is not a leap year')
    else:
        print('This is a leap year')
else:
    print('This is not a leap year')

    
