# for x in range(4):
#     for y in range(4,x,-1):
#         print(y,end=" ")
#     else:
#         print(' ')
# a='*'
# for x in range(1,6):
#     print(x*a)
a=input('enter the line')
b=[a.split]
print(b)
up1=0
low1=0
digi=0
alphs=0
print(up1,low1,digi,alphs)
for x in b:
    if (x.islower):
        low1=low1+1
    elif (x.isupper):
        up1=up1+1
    elif (x.isnumeric):
        digi=digi+1
    else:
        print()
alphs=len(a)-digi
print(up1,low1,digi,alphs,sep='')
