#Instance variables(object): If the value of a variable varies from object to object, then such variables are called instance variables.

class cars:


    def __init__(self,car,milage):
        self.car = car
        self.milage = milage

    def display(self):
        print("car: {},Milage:{}".format(self.car,self.milage))


c1 = cars("Fartuner",13)
c2 = cars("BMW",14)
c1.milage = 16
c1.display()
c2.display()

