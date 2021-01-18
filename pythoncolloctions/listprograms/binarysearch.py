lst=[10,8,7,11,12,6,5]

#element=12

#step 1 sort this list
#  [5,6,7,8,18,11,12]
#   0 1 2 3 4 5 6
#   l           u


#calculate mid=(low+upp)//2=0+6//2=3
#mid=3
#if element>lst[mid]:12>lst[ 12>8

#calculate mid=(low+upp)//2=4+6//2=5
#mid=5
#if element>lst[mid]:12>lst 12>11 low=mid+1=6




#sorting list
lst.sort()
flag=0
#[10,8,7,11,12,6,5]

low=0
upp=len(lst)-1
element=int(input("enter element for searching"))
while(low<=upp):#0<6
    mid=(low+upp)//2 #mid=3
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")