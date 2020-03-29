import numpy as np
from scipy import interpolate
import pylab as pl
#创建数据点集并绘制
x = np.linspace(0, 10, 11)
y = np.sin(x)
pl.plot(x,y,'ro')
#建立插值数据点
xnew = np.linspace(0, 10, 101)
for kind in ['nearest', 'zero','linear','quadratic']:
    #根据kind创建插值对象interp1d
    f = interpolate.interp1d(x, y, kind = kind)
    ynew = f(xnew)#计算插值结果
    pl.plot(xnew, ynew, label = str(kind))
pl.legend(loc = 'lower right')
pl.show()
