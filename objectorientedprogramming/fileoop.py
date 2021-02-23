#print employee details whose designation developer

#no of employees as developer

#print employee details who have highest salary

class Employee:

    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name



f=open("employees.txt","r")
emplist=[]
sallis=[]
for lines in f:
    #1000, anoop, developer, 2, 25000\n
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,salary))

for employee in emplist:
    print(employee)

#print employee details whose designation developer

      #print employee details who have highest salary

for employee in emplist:
    sallis.append(employee.salary)
print(max(sallis))

      #print high salary and name

for employee in emplist:
    sallis.append(employee.salary)
highsal=max(sallis)

for employee in emplist:
    if employee.salary==highsal:
        print(employee)

       #low salary in developer


