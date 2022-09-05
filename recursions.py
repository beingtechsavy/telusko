import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


def greet():
    i=0
    while i<11:
        print("hello")
        greet()
        i+=1