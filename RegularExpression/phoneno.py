#validate phone number

from re import *

phnno=input("enter phone number")


rule="(91)?\d{10}"


matcher=fullmatch(rule,phnno)
if matcher==None:
    print("invalid phone number")
else:
    print("valid phone number")
