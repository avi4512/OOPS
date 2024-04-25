#Single_level Inheritence
class parent:
  
    def phone(self):
        print("Parent Having Realme_c12 phone ")
      
    def bike(self):
        print("Parent having TVS Sport's bike")
      
class child(parent):
  
    def laptop(self):
        print("Child having HP Laptop")
      
#in total now child having all three phone,bike and laptop

c1 = child()
c1.phone()
c1.bike()
c1.laptop()
