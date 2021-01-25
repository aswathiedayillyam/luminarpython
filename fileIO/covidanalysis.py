#state wisw how many confirmed cases
#where the highest case
dict={}
f=open("covid_19_india.csv","r")

for lines in f:
    data=lines.rstrip("\n").split(",")
    #state,confirmedcases
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"
    confirmed_cases=data[8]
    #kerala,2,0,0,0,2
    #kerala:2
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state] = confirmed_cases
for k,v in dict.items():
    print(k,"=====>",v)

#highest
res=sorted(dict,key=dict.get,reverse=True)
print(res)