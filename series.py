# fibonacci series
# def fib(n):
#     a=0
#     b=1
#     for i in range(2,n):
#         c=(a+b)
#         a=b
#         b=c
#         print(c)
# #Arithematic series
# d=int(input("enter the difference"))
# def ap(n):
#     a=1
#     print(a)
#     for i in range(1,n):
#         b=a+d
#         a=b
#         print(b,sep=",")
# ap(10)

# geometric series
a=1
n=1000
def gp(n):
    a=20
    b=10
    print(b)
    for i in range(2,n):
        c=a*b
        b=a
for i in range(1,n):
    a+=gp(i)
gp(n)