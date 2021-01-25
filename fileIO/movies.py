#year wise how many movies released
#highest count of movies released in which year


dict={}
f=open("movies.csv","r")

for lines in f:
    data=lines.rstrip(",").split(",")
    #movie,year
    name=data[1].rstrip("***")
    confirmed_cases=data[2]
    if(name not in dict):
        dict[name]=confirmed_cases
    else:
        dict[name] = confirmed_cases
for k,v in dict.items():
    print(k,"=====>",v)

#highest
#res=sorted(dict,key=dict.get,reverse=True)
#print(res)