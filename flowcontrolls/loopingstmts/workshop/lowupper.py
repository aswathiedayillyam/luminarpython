#num=3
#low=8
#upp=30
#1**3=>1(8,30)
#2**3=>8(8,30)=>8
#3**3=>27(8,30)=>27
#4**3=>64(8,30)
num=int(input("enter num"))#2
low=int(input("enter low"))#8
upper=int(input("enter upper"))#30
for i in range(1,(upper+1)):
    #1**2 (8,30) 2**2=4 3**2=9
    if i**num in range(low,upper):#1 in range(8,30)
        print(i**num)
    else:
        pass

