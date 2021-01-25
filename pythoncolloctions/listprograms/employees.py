employees=[
    [10,"christy","dataanalyst",50000],
    [11, "jhon", "ba", 30000],
    [12, "sab", "dataanalyst",40000],
    [13, "tom", "developer", 40000],
    [14, "jhoni", "developer",40000],
    [15, "sabir", "developer",40000],
    [16, "tom", "developer",40000],
    [17, "jhonis", "developer",47000],
    [18, "jhonis", "developer",32000]
]

#print number of employees in this company
number_of_employees=len(employees)
print("no of employees=",number_of_employees)

#print how much salary company has to raise in month end
total_amount=0
for emp in employees:
    total_amount+=emp[3]
print("total amount=",total_amount)

#group by designation
d_cnt,da_count,ba_count=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
       da_count+=1
    elif emp[2]=="ba":
       ba_count+=1
    else:




#print highest salaried employee
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
hig_salary=max(salary_list)
print(hig_salary)

for emp in employees:
    if emp[3]==hig_salary:
        print(emp)


#print employee name who receives lowest salary whose designation=developer







