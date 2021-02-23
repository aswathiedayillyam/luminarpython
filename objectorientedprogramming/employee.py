class Employee:

    def __init__(self,id,name,desig):
        self.id=id
        self.name=name
        self.desig=desig

    def print_emp(self):
        print(self.name,self.id,self.desig)

obj=Employee(100,"emp1","ba")
obj.print_emp()