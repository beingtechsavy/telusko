class car:
    # wheel is a class variable
    wheels=4
    def __init__(self):
        # these are instance variable
        self.mil=10
        self.com="bmw"
    def update(self,x):
        self.mil=x
c1=car()
c2=car()
c1.update(32)
print(c1.com,c1.mil,c1.wheels)