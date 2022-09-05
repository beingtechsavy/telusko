# from posixpath import supports_unicode_filenames


# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#         print("in init")

#     def config(self):
#         print("config is ",self.cpu,self.ram)
# # hover cursor over the function and then use ctrl + space to see the quality of function.

# com1=computer('i5',16)
# com2=computer('ryzen3',8)
# print(type(com1))
# computer.config(com1)
# computer.config(com2)
# ///////////////////////////////4
# lesson of constructor self and comparing objects
# /////////////////////////////////
class computer:
    def __init__(self):
        self.name="navin"
        self.age=28
    def update(self,x):
        self.age=x
    def compare(self,other):
        if self.age==other.age:
            return True
c1=computer()
c2=computer()
c1.update()
if c1.compare(c2):
    print("they are same")

print(c1.name)