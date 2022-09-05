import numpy as np
import matplotlib.pyplot as pl
from numpy.core.function_base import linspace
a=np.linspace(1,6,50)
b=np.log(a)
pl.plot(a,b,'r',linewidth=3,linestyle='dashed',marker='d',markersize=2,markeredgecolor='blue')
pl.xlabel('this is x axis')
pl.ylabel('this is y axis')
pl.show()