#print highest amoung three
#read 3 num
num1=int(input("no1"))
num2=int(input("no2"))
num3=int(input("no3"))

#num1
if((num1>num2)&(num1>num3)):
    print(num1,"is highest")
elif((num2>num1)&(num2>num3)):
    print(num2,"highest number")
elif((num3>num1)&(num3>num2)):
    print(num3,"highest")
else:
    print("numbers are equal")