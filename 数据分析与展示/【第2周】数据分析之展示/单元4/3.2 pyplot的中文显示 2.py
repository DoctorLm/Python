import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#影响全局
#matplotlib.rcParams['font.family']= 'Songti SC'
#matplotlib.rcParams['font.style']='normal'
#matplotlib.rcParams['font.size']= 20

a = np.arange(0.0,5.0,0.02)
#fontproperties 局部影响
plt.xlabel('横轴: 时间',fontproperties='Songti SC',fontsize=20)
plt.ylabel('纵轴: 振幅',fontproperties='Songti SC',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()
