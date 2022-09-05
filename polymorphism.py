# from ast import operator
# import typing


"""4 ways of polymorphism
duck typing
operator overloading
method overloading
method overridding"""
#duck typing
# x=5
# # x= 'navin'
# class vscodes:
#     def execute(self):
#         print("compiling")
#         print("running")

# class pycharm:
#     def execute(self):
#         print("good day")
#         print("good night")

# class laptop:
#     def code(self,ide):
#         ide.execute()
# ide=pycharm()
# lap1=laptop()
# lap1.code(ide)


# operator overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s4=student(m1,m2)
        return s4
    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1>s2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.m1,self.m2)
a1=student(58,69)
a2=student(60,65)
s4=a1-a2
s3=a1+a2
# student.__add__(a1,a2)
print(s3.m1,s3.m2,s4.m1,s4.m2)
if a1>a2:
    print("s1 wins")
else:
    print("s2 wins")
print(a1.__str__())