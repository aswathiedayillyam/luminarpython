employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"jhon","salary":30000,"exp":2},
    1003:{"id":1002,"name":"danie","salary":35000,"exp":2},
    1004:{"id":1003,"name":"jack","salary":30000,"exp":2}
}

#def print_employee(id=None,prop=None):
#   if id in employee:
#      print(employee[id][prop])
# else:
#    print("employee with this id not exist")

def print_employee(**kwargs):
#    print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
    else:
        print("employee with this id not exist")

print_employee(id=1000,prop="salary")


#nested dictionary
#print(employee[1000])#{"id":1000,"name":"tom","salary":25000,"exp":1}
#print name of employee who have id=1001
#if 1001 in employee:
 #   print(employee[1001]["name"])
#else:
 #   print("eemployee with id not exist")

#salary if
