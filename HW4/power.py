# description: a program that computes exponents without the exponent operation
# name: Cupic, Aleksej
# date: 9.23.19

# function
def power(basenumber,exponent):
    if exponent>0:
        number1=basenumber
        for i in range(0,int(exponent)-1):
            basenumber=basenumber*number1
        answer=basenumber
        return answer
    elif exponent<0:
        number1=basenumber
        for j in range(0,int(-1*exponent)-1):
            basenumber=basenumber*number1
        answer=1/basenumber
        return answer
    else:
        answer=1
    return answer


# main
player=True 
while player==True:
    try:
        basenumber=float(input('Enter the 1st number: '))
        exponent=int(input('Enter the 2nd number: '))
        print(power(basenumber,exponent))
    except ValueError:
        print('Invalid input. Try Again.')

# end
