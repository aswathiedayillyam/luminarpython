lst=[2,5,6,7]

#[18,15,14,13]

#step finding total of this list
#total=20
#[]
#20-2=18
#28-5=15
#


out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)#[18,14]
print(out)
