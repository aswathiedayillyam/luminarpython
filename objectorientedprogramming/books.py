#operator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages


     def __str__(self):
         return str(self.pages)
obj=Book(100)

obj1=Book(200)

print(obj+obj1)#100+100 "hello"+"hai" book + book