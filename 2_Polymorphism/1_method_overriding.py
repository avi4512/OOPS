class vehical:

    def __init__(self,car,model,fuel_type):
        self.car = car
        self.model = model
        self.fuel_type = fuel_type

    def details(self):
        print("Car :{} model : {} fuelType :{}".format(self.car,
                                                             self.model,
                                                             self.fuel_type))

    def max_speed(self):
        print("Max speed is 200")

    def milage(self):
        print("Milage is 10")

class car(vehical):

    def max_speed(self):
        print("Max Speed is 240")

ve1 = vehical("Truck",'xyz','Deseal')
car1 = car("Mahindra",'Xuv500','Petrol')
ve1.details()
ve1.max_speed()
ve1.milage()
car1.details()
car1.max_speed()  #Here car is overriding the method 
car1.milage()
