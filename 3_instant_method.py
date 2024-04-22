class Student:

    def __init__(self,m1,m2,m3):
        self.M1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.M1 + self.m2 + self.m3) / 3


s1 = Student(98,99,97)
s2 = Student(99,98,96)

print(s1.avg())
print(s2.avg())
