#functional programming is used for reduding coding length



def add(num1,num2):
    return num1+num2

#using lambda functions

add=lambda num1,num2: num1+num2
print(add(100,200))

def sub(num1,num2):
    return num1-num2

#using lambda functions

sub=lambda num1,num2: num1-num2
print(sub(200,100))

#cube of a number

cube=lambda num: num**3
print(cube(2))

#to check number even or not

even=lambda num: num%2==0
print(even(20))


#map()
#filter()
#reduce()-reduce to a single value

lst=[1,2,3,4,5,6]

def square(num):
    return num**2

#sqlist=list(map(square,lst))
sqlist=list(map(lambda num: num**2,lst))
#function,iterables

print(sqlist)

lst=[1,2,3,4,6]
#num<5 num-1 num+1

numlist=list(map(lambda num: num-1 if num<5 else num+1 if num>5 else num,lst))
print(lst)

evens=list(filter(lambda num: num%2==0,lst))
print(evens)

#odd numbers

evens=list(filter(lambda num: num%2!=0,lst))
print(evens)

names=["india","pak","aus","eng","sa","srilanka"]


