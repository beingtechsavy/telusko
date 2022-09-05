from functools import *
nums=[]
for  i in range (100):
    nums.append(i)
print(nums)
even=list(filter(lambda n:n%2==0,nums))
print(even)
doubles=list(map(lambda n:n*2,even))
print(doubles)
sum=reduce(lambda x,y:x+y,doubles)
print(sum)