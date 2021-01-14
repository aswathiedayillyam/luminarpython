#num=123
#321
num=int(input("enter number"))#123
while(num!=0):#123!=0 12!=0 1!=0 0!=0
    digit=num%10#digit=123%10=3 12%10=2 1%10=1
    print(digit,end="")#321
    num=num//10#num=123//10=12 12//10=1 1//10=0