lst=[10,11,12,13,14,15]
element=int(input("enter element you want to search"))
flag=0
cnt=0
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print("element not found")
else:
    print("element found",cnt)
