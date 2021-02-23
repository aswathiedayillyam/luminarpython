class Swift:
    def drive(self):
        print("driving swift car")

class Sonet:
    def drive(self):
        print("driving sonet")

class Person:
    def start(self,car):
        car.drive()

sw=Sonet()
p=Person()
p.start(sw)


#duck typing is a concept related to dynamic typing,

#if it walks like a duck and it
