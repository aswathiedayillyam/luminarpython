#2
#2+22=24

#3
#3+33+333=359

#4
#4+44+444+4444=

num=input("enter number")#"2"
data=""
res=0
for i in range(1,(int(num)+1)):#i=1
    data=num*i#"2"*1="2" "2"*2
    res=res+int(data)
print(res)
