# description: A program that calculates BMI
# author: Cupic, Aleksej
# date: 9.11.2019

# function computeBMI 
def computeBMI(height,weight):
    heightnumber=height/39.37
    weightnumber=weight/2.205
    bodymassindex= weightnumber/heightnumber**2
    return bodymassindex
    
# main section
print('This is a program that calculates BMI')
height_in_ft=int(input('Enter the feet part of your height:'))
height_in_in=int(input('Enter the inches part of your height:'))
weight=int(input('Enter your weight in pounds:'))
height=height_in_ft*12+height_in_in
print('Height in inches:',height)
print('Body mass index:',computeBMI(height,weight))

# if conditionals for BMI meaning
if computeBMI(height,weight)>25:
    print('Overweight')
elif computeBMI(height,weight)>18.5:
    print('Normal weight')
else:
    print('Underweight')
    