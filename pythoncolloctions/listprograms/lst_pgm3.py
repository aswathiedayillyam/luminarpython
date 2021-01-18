lst=[10,11,12,13,14,15,16,17]
#even numbers=>evelist
#odd numbers=>oddlist
#find total of evenlist,totaloddlist

evnlist=list()
oddlist=list()
for num in lst:
    if(num%2==0):
        evnlist.append(num)
    else:
        oddlist.append(num)
print(oddlist)
print(evnlist)
print("oddsum",sum(oddlist))
print("evensum",sum(evnlist))
