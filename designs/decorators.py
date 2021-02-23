#def sub(num1,num2):
#   return num1,num2
#print(sub(10,20))



def subtract(func):

    def inner(num1,num2):
        if num1 < num2:
            (num1, num2) = (num2, num1)
        return function(num1,num2)
    return inner

@subtract
def sub (num1,num2):

    return num1-num2

data=sub(10,20)
print(data)

#decorator used for aditional feature
