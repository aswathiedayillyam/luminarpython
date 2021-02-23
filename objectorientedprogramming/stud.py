#student class
class Student:
    def setStudent(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name
    def get_student(self):
        print(self.rol,",",self.course,",",self.name)

obj=Student()
obj.set_student(1001,"django","akhil")
#obj.get_student()

print(obj.course)
print(obj.rol)


#set_student()
#initializing instance variables
#instance variables?
   #instants variables are prepended with self keyword

#we can acess instance variable outside class by using reference
#inside class self

#employee clss??
#eid,ename,desig,salary
#initialize
#print

#have to create minimum 2 objects.


#queue

#                     constructor
#duty of constructor initializing instance variable
#constructor name always class name in java and c++ in python constructor name is --init__()

#constructor automatically invoked during object creation
class Student:
    def __init__(self,ro,course,name):

            self.rol= ro
            self.course = course
            self.name = nam

    def get_student(self):
            print(self.rol, ",", self.course, ",", self.name)

    obj=Student(1001,"django","akhil")

    # obj.get_student()

    print(obj.course)
    print(obj.rol)