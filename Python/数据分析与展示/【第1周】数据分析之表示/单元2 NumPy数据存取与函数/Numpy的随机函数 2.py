import numpy as np
#Numpy的随机函数
#np.random的随机数函数(1)
#rand(d0,...,dn)    根据d0-dn创建随机数数组,浮点数[0,1]均匀分布
#randn(d0,...,dn)   根据d0-dn创建随机数数组,标准正态分布
#randint(low[,high,shape])  根据shape创建随机整数或整数数组,范围是[low,high]
#seed(s)    随机数种子,s是给定的种子值
print("np.random的随机数函数(1)")
a = np.random.rand(3,4,5)
print("np.random.rand(3,4,5)\n",a)
a = np.random.randn(3,4,5)
print("np.random.randn(3,4,5)\n",a)

np.random.seed(10)
a = np.random.randint(100,200,(3,4))
print("np.random.seed(10)")
print("np.random.randint(100,200,(3,4))\n",a)

np.random.seed(10)
a = np.random.randint(100,200,(3,4))
print("np.random.seed(10)")
print("np.random.randint(100,200,(3,4))\n",a)

#np.random的随机数函数(2)
#shuffle(a) 根据数组a的第1轴进行随排列，改变数组x
#permutation(a) 根据数组a的第1轴产生一个新的乱序数组，不改变数组x
#choice(a[,size,replace,p]) 从一维数组a中以概率p抽取元素，形成size形状新数组replace表示是否可以重用元素，默认False
print("np.random的随机数函数(2)")
print("shuffle(a) 根据数组a的第1轴进行随排列，改变数组x")
np.random.seed(10)
b = np.random.randint(100,200,(3,4))
print("np.random.seed(10)")
print("np.random.randint(100,200,(3,4))\n",b)
np.random.shuffle(b)
print("np.random.shuffle(b)\n",b)
np.random.shuffle(b)
print("np.random.shuffle(b)\n",b)

print("permutation(a) 根据数组a的第1轴产生一个新的乱序数组，不改变数组x")
np.random.seed(10)
b = np.random.randint(100,200,(3,4))
print("np.random.seed(10)")
print("np.random.randint(100,200,(3,4)\n",b)
print("np.random.permutation(b)\n",np.random.permutation(b))
print("np.random.randint(100,200,(3,4)\n",b)
print("#choice(a[,size,replace,p])从一维数组a中以概率p抽取元素，形成size形状新数组replace表示是否可以重用元素，默认False")
b = np.random.randint(100,200,(8,))
print("np.random.randint(100,200,(8,))\n",b)
print("np.random.choice(b,(3,2))\n", np.random.choice(b,(3,2)) )
print("np.random.choice(b,(3,2),replace=False)\n", np.random.choice(b,(3,2),replace=False) )
print("np.random.choice(b,(3,2),p=b/np.sum(b))\n", np.random.choice(b,(3,2),p=b/np.sum(b)) )

#np.random的随机数函数(3)
#uniform(low,high,size)产生具有均匀分布的数组，low起始值，high结束值,size形状
#normal(loc,scale,size)产生具有正态分布的数组,loc均值,scale标准差,size形状
#poisson(lam,size)产生具有泊松分布的数组,lam随机事件发生率,size形状
u = np.random.uniform(0,10,(3,4))
print("np.random.uniform(0,10,(3,4))\n",u)
n = np.random.normal(10,5,(3,4))
print("np.random.normal(10,5,(3,4))\n",n)
n = np.random.poisson(100,(3,4))
print("np.random.poisson(100,(3,4))\n",n)
