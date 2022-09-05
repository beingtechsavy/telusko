class computer:
    def __init__(self):
        self.age=28
        self.name="Navin"
        print("hello world")
    def compare(self,other):
        return self.age == other.age
    def update(self):
        self.age=30


c1=computer()
c2=computer()
c1.update()
if c1.compare(c2):
    print("my name is arpan")
