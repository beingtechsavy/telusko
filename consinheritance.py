class A():
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature1 working fine....")
    def feature2(self):
        print("feature2 working fine....")
    
class B():
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("feature-b working fine....")
    def feature4(self):
        print("feature4 working fine....")
class c(B,A):
    def __init__(self):
        super().__init__()
        print("in c init")
    def feat(self):
        super().feature4()
a1=c()
a1.feature1()