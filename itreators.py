class Topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        while self.num<=1000:
            val=self.num
            self.num+=1
            return val
        else:
             raise StopIteration
        

valuez=Topten()        
for i in valuez :
    print(i)