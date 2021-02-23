#7[1,7]
#13[1,13]
num=int(input("enter num to check prime or not"))#9
#2,3,4,5,6,7,8
flag=0
for i in range(2,num):#2
    print(i)
    if(num%i==0):#9%2==0
        flag=flag+1#flag=1
        break

    else:
        pass
if(flag==0):
    print("prime number")
else:
    print("not a prime number")
