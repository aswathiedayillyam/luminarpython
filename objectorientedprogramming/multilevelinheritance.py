class Parent:
    def m1(self):
        print("inside parent1")
class Child:
    def m2(self):
        print("inside child")
class Subchild(Child):
    def m3(self):
        print("inside sub child")
obj=SubChild()
obj.m3()
obj.m2()
obj.m1()
