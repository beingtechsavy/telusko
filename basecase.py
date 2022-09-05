"""we make a case known as exit case ehose value is already known
recursive code for factorial"""
# for each recursive call new memory location is allocated
# def binod(n):
#     if n<=1:
#         print("program finished",n)
#         return
#     else:
#         binod(n-3)
# binod(8)
# def babula(n):
#     if n==1:
#         print('the program executed successfully')
#         return
#     elif n%2==0:
#         print(n)
#         babula(n/2)
#     else:
#         babula(n/1)
# babula(8)
# in iterations
# str2='arpan'
# for i in range(4,-1,-1):
#     print(str2[i])
# with recursions
# def rev(str):
#     if len(str)==0:
#         return str
#     else:
#         print(str[1:])
#         print(str[0])
#         return rev(str[1:])+str[0]
# rev(str2)
# print(rev(str2))
# def fbi(s):
#     if s<=1:
#         return 1
#     else:
#         return fbi(s-1)+fbi(s-2)
# for i in range(34):
#     print(fbi(i))
# def sume(n):
#     if n==1:
#         return 1
#     return sume(n-1)+1
#     print(sume(10))
# print(sume(10)) 
# fast power
# def multiplior(a,b):
#     if b==1:
#         return a
#     if b%2!=0:
#         return a*multiplior(a,b-1)
#     if b%2==0:
#         return multiplior(a**2,b/2)

# print(multiplior(3,4))
# no of paths in a m*n grid
# def paths(a,b):
#     if a==1 or b==1:
#         return 1
#     return paths(a-1,b) + paths(a,b-1)
# print(paths(23,4))
# def findoutput():
#     l='earn'
#     x=' '
#     l1=[]
#     count=1
#     for i in l:
#         if i in ['a','e','i','o','u']:
#             x+=i.swapcase
#         else:
#             if count%2!=0:
#                 x+=str(len(l[:count]))
#             else:
#                 x+=i
#             count=count+1
#     print(x)
# findoutput()
# l1=['abc','123']
# for i in l1:
#     l1.append(i)
#     print(l1)
# def func1():
#     global a
#     return a
# a=11
# print(func1())
# p=(1,)
# print(p)
# a,b=4,2.5
# print(b//2**2)
# print(b%a)
a='  '
# b=a[1:3]D
# print(b)
# if a.isspace():
#     print(True)
# a=chr(69)
# print(a)
# str='Hello World! Hello Helplo'
# print(str.count('Hello',12,25))
# b=str.replace('py','koka')
# print(str[:-4])
# p=[5,6,8,2,1,-65]
# a='aroan is a boy'
# b=a.split()
# print(b)
# a=[1,2,3]/
# 11=[20,30]
# k={'a':34,'f':46}
# print('f' in k)
# s=k.copy()
# print(s)
# the key i.e the first part has to be of the type number tuple and string.
# a='string'
# # b='bot'
# a=(2,4,5,'arpan')
# a+(60,)
# print(a)
# del a
# print(a[-1])
# a=tuple()
# print(a)
# original = {1: 'geeks', 2: 'for'}
# new={"arpan":23}
# copying using copy() function
# new = original.copy()

# removing all elements from the list
# Only new list becomes empty as copy()
# does shallow copy.

# print('new: ', new)
# print('original: ', original)
# x=50
# def func(x):
#     return x,2
# a=func(x)
# print(type(a))
# print(x)
def Interest(p,c,t=2,r=0.09):
    return p*t*r
Interest(r=0.05,5000,c=5)