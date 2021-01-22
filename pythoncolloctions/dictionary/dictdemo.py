expenses={"jan20":30000,"feb20":25000,"march20":28000,"april20":25000,"may20":22000
          }
          print(expenses["march"]) #march is key
#values stored in dict in the form key value pair
#how do we fetch value from dictionary
#is to possible to store duplicate key,key must be unique

#chk for june 20
print("june20" in expenses)

#adding new key value pairs
#june20:25000
expenses["june20"]=25000
print(expenses)

print("march20" in expenses)
expenses["march20"]-=3000
print(expence["march20"])
