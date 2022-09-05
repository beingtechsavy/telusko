from abc import ABC,abstractmethod

"""the computer is taken as a parent referendum for the properties and charachteristics of the sub class like laptop mobile and whiteboard."""
class computer(ABC):                
    def __init__(self):
        self.length=9
        self.breadth=10
    
    @abstractmethod
    def process(self):
        return self.breadth*self.length
class laptop(computer):
    def process(self):
        print("its running")
class mobile(computer):
    def start(self):
        print("its running")
class whiteboard(computer):
    def scribble(self):
        print("info taken")        
a=laptop()
a.process()

# a.process()
# b.process()
