#keys used
#class(design pattern is called class)
#object
#reference
#class plan,design,blueprint,template
#object:real world entity
class Person:
    #methods
    def setPerson(self,age,name):
        self.age=age
        self name=name

    def printPerson(self):
        print("name",self.name)
        print("age=",self.age)

#we created a class person(self.name.self.age)
#setperson()
#printPerson()

obj=person()
obj.setPerson(25,"ajay")
obj.printPerson()

obj1=person()
obj1.setPerson(25,"vijay")
obj1.printPerson()
