f=open("demo","r") #read mode "r"

dict={}

for line in f:
    #Amid a raging controversy over
    words=line.rstrip("\n").split(" ")
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)

#key,value
