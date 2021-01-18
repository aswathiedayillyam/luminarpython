lst=[1,2,3,5]
#    l     u
low=0
upp=len(lst)-1
element=int(input("enter element"))
while(low<upp):
    tot=lst[low]+lst[upp]
    if(element==tot)
        print(lst[low],lst[upp])
        breakelse:
        low+=1




num=10
num=int(input("enter number to find pairs"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])