import numpy as np

#索引切片
a = np.array([9,8,7,6,5])
print(a[2])
print(a[1:4:2]) #起如编号：终止编号（不含）:步长3元素冒号":"分割

a = np.arange(24).reshape((2,3,4))
print(a)
print(a[1,2,3])
print(a[0,1,2])
print(a[-1,-2,-3])

print(a[:,1,-3])    #:选取一个维度
print(a[:,1:3,:])   #每个维切片方法与一维数组相同
print(a[:,:,::2])   #每个维用步长进行跳跃切片
