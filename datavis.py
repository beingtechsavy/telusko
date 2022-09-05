from matplotlib.pylab import *
import numpy as np
# l=[1,23,45,5]
# a=np.array(l)
# print(type(a))
# print(a.shape)
# print(a.itemsize)
# print(a.dtype)
a=np.linspace(1,10 ,100)
b=np.sin(a)
plot(a,b)
xlabel('this is on x axis ')
ylabel('this is on y axis ')
show()
