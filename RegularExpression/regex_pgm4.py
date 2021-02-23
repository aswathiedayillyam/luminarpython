#a,k  first character must be a alphabet btw a-k
#second character must be a number or digit divisible by 3
#followed by any number of character

#z6kbb false
#c8rttt false
#a9bk true


from re import *
varname=input("enter variable name")

rule="[a-k][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid variable name")
else:
    print("valid variable name")
