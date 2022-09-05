class student():

    school='telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschoolname(cls):
        return cls.school
    @staticmethod
    def info():
        return("this is student class...")
s1=student(34,67,32)
s2=student(89,32,12)
s3=student(89,89,89)
print(s1.avg())
print(s2.avg())
print(s3.avg())
print(student.getschoolname())
print(student.info())

