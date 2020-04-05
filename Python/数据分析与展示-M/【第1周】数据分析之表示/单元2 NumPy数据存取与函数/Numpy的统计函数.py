import numpy as np
#NumPy的统计函数
#NumPy直接提供的统计类函数
#np.* np.std() np.var() np.average()
#np.random的统计函数(1)
#sum(a,axis=None)   根据给定轴axis计算数组a相关元素之和，axis整数或元组
#mean(a,axis=Non3)  根据给定轴axis计算数组a相关元素的期望，axis整数或元组
#average(a,axis=None,weights=None)  根据给定轴axis计算数组a相关元素的加权平均值
#std(a,axis=None)   根据给定轴axis计算数组a相关元素的标准差
#var(a,axis=None)   根据给定轴axis计算数组a相关元素的方差
#axis=None是统计函数的标配参数
print("np.random的统计函数(1)")
a = np.arange(15).reshape(3,5)
print("a:\n",a)
print("np.sum(a)\n",np.sum(a))
print("np.mean(a,axis=1)\n",np.mean(a,axis=1))
print("np.mean(a,axis=0)\n",np.mean(a,axis=0))
print("np.average(a,axis=0,weights=[10,5,1])\n",np.average(a,axis=0,weights=[10,5,1]))
print("np.std(a)\n",np.std(a))
print("np.var(a)\n",np.var(a))

#np.random的统计函数(2)
#min(a) max(a)  计算数组a中元素的最小值、最大值
#argmin(a) argmax(a)    计算数组a中元素最小值、最大值的降一维后下标
#unravel_index(index,shape) 根据shape将一维下标index转换成多维下标
#ptp(a) 计算数组a中元素最大值与最小值的立差
#median(a)  计算数组a中元素的中位数(中值)
print("np.random的统计函数(2)")
b = np.arange(15,0,-1).reshape(3,5)
print("b:\n",b)
print("np.max(b)\n",np.max(b))
print("np.argmax(b)\n",np.argmax(b))
print("np.unravel_index(np.argmax(b),b.shape)\n",np.unravel_index(np.argmax(b),b.shape) )
print("np.ptp(b)\n",np.ptp(b))
print("np.median(b)\n",np.median(b))
