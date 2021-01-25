students=[
    [10,"ajay","bca",250],
    [11,"vijay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",100],
    [15,"jain","mca",250]

]

#print(students[0])
#print(students[0],[1])

#student name only
#for stud in students:
   # print(student)
 #   print(stu[1])


#print student names whose total >240
#for stud in students:
 #   if stud[3]>240:
  #      print(stud[1])


#print total sum of total
marks=0
for stud in students:
    marks=marks+stud[3]
print("total =",marks)

#calculate total of bca and mca separately
mtotal,btotal=0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
        print("mca total=",mtotal)
        print("bca total=",btotal)

