#regular expressions
#used  to pattern matching

#step1- import re module
from re import *

pattern="ab"
#find how many ab
matcher=finditer(pattern,"ababababababab")
cnt=0
for match in matcher:
    print(match.start())#position
    print(match.group())
    cnt+=1
print(cnt)


