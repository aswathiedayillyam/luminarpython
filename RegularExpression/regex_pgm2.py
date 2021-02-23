from re import *


#pattern='[ab]'#either a or b
pattern='[a-z]'#chk for lower case a to z
#pattern='[0-9]' will chk for digit
#pattern='[^0-9]' #except 0 to 9
#pattern='[a-zA-Z0-9]'all words and numbers except underscore,space etc
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())




#predefined characters
pattern="\s" #chk for spaces
pattern="\d" #chk for digit
pattern="\D" #[^0-9]
pattern='\z' #chk for all words
pattern="\w" #except words

matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start(),"->",match.group())