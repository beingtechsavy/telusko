# d={'dog':'cat','bag':'chug','slug':'life'}
# d2={'dog':'45664','bag':'chug','films':'hollywood'}
# d.update(d2)
# print(d)    
di={'jan':'31','march':'31','june':'31','august':'31','october':'31','december':'31','february':'28','april':'30','july':'30','september':'30','november':'30'}
# a=input("enter the month name")
# b=input("enter the no of days")
# # ############
# l=[di.keys()]
# l.sort
# print(l)
# ##########
# for i in di:
#     if di[i]=='31':
#         print(i)
#33333333333333333333333
# for i in sorted(di.keys()):
#     print(i,di[i])
#4 
for i in sorted(di,key=di.get):
    print(i,di[i])   
# here key stands for the key element passing through the loop.
# here we see the loop is concentrated about the values of the keys and not keys itself.