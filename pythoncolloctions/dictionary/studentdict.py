#print_data(rol=1000) print name of student rol=1000
#print_data(rol=1001,property="course") #name,course

f=open("students","r")
students={}
for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")

    if id not in students:
        students[id]={"id":id,"name":name,"total":total,"course":course}

def print_student_data(**kwars):
    id=kwars["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwars:
            prop=kwars["prop"]
            print(students[id][prop])
    else:
        print("there no student exist with this id")

print_student_data(id="1001",prop="total")





#operators
#i/o
#flow controls
#list,set,tuple,dict,file

#oop

