#read two numbers print true if two numbers =100
# and print true either num1 is 100 or num2 is 100
#num1,num2=50,50
#
num1=int(input("enter num1"))
num2=int(input("enter num2"))

if((num1+num2==100)|(num1==100)|(num2==100)):
    print("true")
else:
    print("false")