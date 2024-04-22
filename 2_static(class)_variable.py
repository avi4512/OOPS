# static variable or (class variable) :
# if you change the static variable it changes the all values in the all the object;s value

class cars:

    wheels = 4

    def __init__(self,car,milage):
        self.car = car
        self.milage = milage

    def display(self):
        print("car: {},Milage:{},Wheels:{}".format(self.car,self.milage,cars.wheels))


c1 = cars("Fartuner",13)
c2 = cars("BMW",14)
c1.milage = 16    #it changes only the Particular mention object
cars.wheels = 6   #it changes in the whole class object's
c1.display()
c2.display()
