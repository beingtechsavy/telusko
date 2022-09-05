from array import *
vals=array('i',[12,123,156,45])
vals.reverse()
print(vals)
for e in vals:
    print(e)
# for i in range(len(vals)):
#     print(vals[i])
# for i in range(4):
#     print(vals[i])
newarr=array(vals.typecode,(a for a in vals))
print(newarr)