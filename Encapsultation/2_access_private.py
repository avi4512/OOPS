'''We can access Private members using 3 Way's
1. Public method's To access Private members
'''
class details:

    def __init__(self,id,name,ac_no):
        self.id = id              #public(access anywhere outside class)
        self._name = name         #Protect(access with in the class)
        self.__ac_no = ac_no      #private(with in class and its subclass)

    def info(self):
        print("id : {} name : {} ac_no : {}".format(self.id,self._name,self.__ac_no))

obj1 = details(100,'Avi',4512)

obj1.info()

#2 . Name Mangling
class details:

    def __init__(self,id,name,ac_no):
        self.id = id              #public(access anywhere outside class)
        self._name = name         #Protect(access with in the class)
        self.__ac_no = ac_no      #private(with in class and its subclass)


obj1 = details(100,'Avi',4512)

print("id:",obj1.id)
print("Name:",obj1._name)   #protect
print("Account no:",obj1._details__ac_no)  #private


#3.Getter Setter Methods
class details:

    def __init__(self,id,name,ac_no):
        self.id = id              #public(access anywhere outside class)
        self._name = name         #Protect(access with in the class)
        self.__ac_no = ac_no      #private(with in class and its subclass)

    def get_ac_no(self):
        return self.__ac_no

    def set_ac_no(self,ac):
        self.__ac_no = ac


obj1 = details(100,'Avi',4512)

#retriving(Getting) the Data
print("Name:",obj1._name,"Acc_no:",obj1.get_ac_no())

#Setting (modifing) data
new_acc = int(input("Enter the Acc_no:"))
obj1.set_ac_no(new_acc)
print("Name:",obj1._name,"Acc_no:",obj1.get_ac_no())



