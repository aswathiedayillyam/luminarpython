#how to create empty list
# lst=[]
lst=list()#creating an empty list
#method for adding an element to list
#lst[0]=50

#lst.append(50)
#lst.append(60)
#print(lst)

#0 to 50
lst=list()
for i in range(1,51):
    lst.append(i)
#print(lst)


high=max(lst)
print(high)
mini=min(lst)
print(mini)


#total sum
total=sum(lst)
print(total)
