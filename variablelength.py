#variable length argument method


def add(*args):
    return sum(args)

total=add(10,20,30,40,50)
print(total)

#*args-any number of arguments in the form of touple.


#def print_data(*args):
 #   print(args)
#print_data("ajay","kakkanad","Thrissure")

def print_data(**kwars):
    print(kwars)

print_data(name="ajay",worklocation="kakkanad",home="thrissur")





#