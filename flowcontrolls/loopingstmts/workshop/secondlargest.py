num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))

if ((num1>num2)&(num1>num3)):
    #first number num1
    #possibility for num2 num3
    if(num2>num3):
        print(num2,"is second largest")
        print("sorted order",num1,num2,num3)
    else:
        print(num3,"second largest")
        print("sorted order", num1, num3, num2)
elif((num2>num1)&(num2>num3)):
     #second num1,num3
     if(num1>num3):
         print(num1,"second")
         print("sorted order", num2, num1, num3)
     else:
         print(num3,"second")
         print("sorted order", num2, num3, num1)
elif((num3>num2)&(num3>num1)):
     #second num2 num1
     if (num1 > num2):
         print(num1,"second")
         print("sorted order", num3, num1, num2)
     else:
         print(num2,"second")
         print("sorted order", num3, num2, num1)
