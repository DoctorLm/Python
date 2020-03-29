import matplotlib.pyplot as plt

#pyplot的绘图区域
plt.subplot(211)
plt.plot([0,2,4,6,8],[1,3,5,6,9])
plt.ylabel("grade")
#plt.savefig('test',dpi=600)
plt.axis([-1,10,0,10])
'绘图区域'
plt.subplot(212)
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel("grade")
#plt.savefig('test',dpi=600) #默认PNG
plt.axis([-1,10,0,10])
plt.show()
