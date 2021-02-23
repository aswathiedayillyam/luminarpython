#lst[10,20,30,40]
#squares=list(map(lambda num:num**2))
#or
#squares=[num**2 for num in lst]
#print(squares)
lst=[[10,20],[30,40],[50,60]]
#convert this nested list to 10,20,30,40,50,60
op=[for ls in lst for num in ls]

#find even number from given listcompre