class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("the config is ", self.cpu,self.ram)
com1=computer('i5',16)
com2=computer('ryzen 3',8)
# print(type(com1))
# computer.config(com1)
com1.config()
com2.config()