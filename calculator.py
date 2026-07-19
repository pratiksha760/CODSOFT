def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num1
def division(num1,num2):
    return num1/num2
def modul(num1,numm2):
    return num1%numm2
def calci():
    while True:

       num1=int(input("Enter a number = "))
       num2 = int(input("Enter a number = "))
       operator = input("Enter operator(+,-,*,/,%) = ")
       if operator =='+':
           addition =add(num1,num2)
           print(f"{num1} + {num2} = {addition} ")
       elif operator =='-':
            substraction = subtract(num1,num2)
            print(f"{num1} - {num2} = {substraction} ")
       elif operator=='*':
            multiplication =multi(num1,num2)
            print(f"{num1} * {num2} = {multiplication} ")
       elif operator=='/':
            dividetion =division(num1,num2)
            print(f"{num1} / {num2} = {dividetion} ")
       elif operator=='%':
            mudulas =modul(num1,num2)
            print(f"{num1} % {num2} = {mudulas} ")
       else:
            print("please enter valid operator ")

calci()