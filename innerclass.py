class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        self.lap.show()
        print(self.name,self.rollno)

    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram='8gb'
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student('navin',2)
s2=student('jenny',3)
s1.show()
print(s1.lap.brand)
lap1=student.laptop()
# lap1.show()