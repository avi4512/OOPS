class details:

    def __init__(self,id,name,ac_no):
        self.id = id              #public(access anywhere outside class)
        self._name = name         #Protect(access with in the class)
        self.__ac_no = ac_no      #private(with in class and its subclass)


obj1 = details(100,'Avi',4512)
