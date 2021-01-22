employe={"id":100,"ename":"ajay","exp":2,"salary":35000}
if("salary" in employe):
    print(employe["salary"])

#print employee name
print(employe["ename"])

#chk gender key
if("gender" in employe):
    print("exit")
else:
    employe["gender"]="male"
print(employe)

#if employe salary <35000 add 5000 rs more
if(employe["salary"]<=35000):
    employe["salary"]+=5000
    print(employe)