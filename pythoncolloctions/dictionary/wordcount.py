#word="hello hai hello hai hello"
#word count
#hello:3, hai:2

#movie data set
#covid analysis

text="hai hello hai hello"
words=text.split(" ")
#words=[hai,hello,hai,hello]
dict={}
#key value
#hai 2
#hello 2


for word in words:#word=hai
    if(word not in dict):#if hai not in dictionary hai:1
        dict[word]=1
    else:
        dict[word]+=1 #dict["hello"] 1+1=2

print(dict)
