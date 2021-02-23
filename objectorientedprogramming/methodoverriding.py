class Parent:
    def mobile(self):
        print("nokia5310")
class Child(Parent):
    def mobile(self):
        print("iphone")

c=Child()
c.mobile()

c=Parent()
print(c) #print an object while printing object __str__() will invoke

