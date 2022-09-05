from math import *
#     if i%10==0 and i%7==0:
#         continue
#     print(i)
# a=0
# s=0
# while a<=5:
#     s=s+a
#     a=a+1
# n=int(input("enter the last numbe
def strange(x):
    if x==1:
        return 1
    else:
        return (x*x)*strange(x-1)
print(strange(10))

    