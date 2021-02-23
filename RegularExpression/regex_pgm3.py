#quantifiers
#how much quantity is there
from re import *

pattern="a+" #any number of a excluding 0 number of a
pattern="a*" # any no of a including 0 number of a
pattern="a?" #occuring single a
pattern="a{2}" #2 a one grp
pattern="a{2,4}"#min 2 a and max 4 a




matcher=finditer(pattern,"aaaaaaabababaabaaa")
for match in matcher:
    print(match.start(),"=>",match.group())


#fundamentals

#rules

#eg: vehicle registation pattern


#[1,2,3,4,5,6] [6,1,2,3] chek it is rotation array(1 list is continuation of next array?)
