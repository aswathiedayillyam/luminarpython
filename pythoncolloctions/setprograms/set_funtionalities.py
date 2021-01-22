st1={10,20,30,40}
st2={30,40,50,60,70,80}

#union
#  10 20 30 40 50 60 70 80
unset=st1.union(st2)
print(unset)        #not come duplicates

#intersection
inter=st1.intersection(st2)
#common elements
print(inter)

#difference
#set2 elements remove from the set 1  elements
diff=st1.difference(st2)
print(diff)
#{10,20}


#assesment
#task1
students=["name1","name2","name3","name3"]
fail=["name1","name2"]
#create passed student set


