#in python not Support The Concept of Method Overloading 

class MethodOverloading:

    def sum(self,a=None,b=None,c=None):

        if a != None and b !=None and c!=None:
            res = a + b + c
            return res
        elif a !=None and b !=None:
            res = a + b
            return res
        elif a !=None:
            res = a
            return res

obj1 = MethodOverloading()
print(obj1.sum(10,20,30))
print(obj1.sum(10,20))
print(obj1.sum(10))
