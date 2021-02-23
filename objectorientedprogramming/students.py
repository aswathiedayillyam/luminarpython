class Students:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name



obj=Students(100,"akshay","django",140)
obj1=Students(101,"akhil","mean",140)
obj2=Students(102,"ashil","django",145)

#print(obj)
#print list of django students only

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
total=0
for stud in slist:
   #print(stud)
   if stud.course=="django":
       total+=stud.total
       #print(stud.name)
       print(total)


#total of django students

