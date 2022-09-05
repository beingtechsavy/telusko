# def calcresult(i):
#     while i>1:
#         if i%2==0:
#             x=i%2
#             i=i-1
#         else:
#             i=i-2
#             x=i
#         print(x**2)
# calcresult(9)
# d=[]
# if d:
    # print(True)
# else:
    # print(False)
# p=(1,10)
# q=0
# r=[]
# if p or q and r:
#     print(True)
# else:
#     print(False)
# l=['ABC','XYZ','pqr']
# x=[]
# for i in l:
#     x=i.lower()
#     print(x,end='\t')
# print(12,1,5545,484)
def changelist():
    l=[]
    l1=[]
    l2=[]
    for i in range(1,10):
        l.append(i)
    for i in range(10,1,-2):
        l1.append(i)
    for i in range (len(l1)):
        l2.append(l1[i]+l[i])
    l2.append(len(l)-len(l1))
    print(l2)
changelist()