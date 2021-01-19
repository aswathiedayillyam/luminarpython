lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
#[10,20,21,22,51,52,53,54,55,56]
#flat10 operation
numlist=[]
for sublist in lst:
    #[10,20]sublist
    for num in sublist:
        numlist.append(num)
print(numlist)