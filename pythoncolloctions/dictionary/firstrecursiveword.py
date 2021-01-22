pattern="ABABBACEEEEE"
#find first recursive character A
dict={}
for ch in pattern:
    #print(ch)
    if ch not in dict:#a:1,b:1
        dict[ch]=1
    else:
        #print(ch,"is first recursive character")
        #break
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)
#maximum
#sort based on value

print(dict.get("E"))
result=sorted(dict,key=dict.get,reverse=True)
print(result[0])
