import math
# help(math)
# you can use "from math import *"
# to import all
# if we do "from math import sum as s 
# then s is known as "alias name" "
from random import *
# help(random)
# returns a random integer between 0 and 1
# help(randint)
# randint includes both max and min value
# returns a random integer between given values
# print(randrange(1,10,3))
# it return a random integer between the given values with interval of s (3)
# for evaluating random always take the min and max values and then evaluate the code
# for j in range(2):
#     for i in range(1,5):
#         print(10+random()*5)
a=randint(0,3)
c=['delhi','mumbai','chennai','kolkata']
for i in c:
    for j in range(1,a):
        print(i)