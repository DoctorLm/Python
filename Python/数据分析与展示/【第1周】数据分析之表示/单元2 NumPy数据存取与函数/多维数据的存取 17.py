import numpy as np

#多维数据的存取
#a.tofile(frame,sep='',format='%s')
#frame:文件、字符串
#sep:数据分割字符串，如果是空串，写入文件为二进制。
#format:写入数据的格式。

a = np.arange(100).reshape(5,10,2)
a.tofile("test.dat",sep=',',format='%d')
a.tofile("test.dat",format='%d') #二进制文件

#np.fromfile(frame,dtype=float,count=-1,sep='')
#frame:文件、字符串
#dtype:读取的数据类型
#count:读入元素个数,-1表示读入整个文件
#sep:数据分割字符串，如果是空串,写入文件为二进制
a = np.arange(100).reshape(5,10,2)

a.tofile("test.dat",sep=',',format='%d')
c = np.fromfile("test.dat",dtype=np.int,sep=",")
print(c)

a.tofile("test.dat",format='%d')
c = np.fromfile("test.dat",dtype=np.int).reshape(5,10,2)
print(c)

#NumPy的便捷文件存取
#np.save(fname,array)或np.savez(fname,array)
#frame:文件名，以.npy为扩展名，压缩扩展名为.npz
#array:数组变量
#np.load(fname)
#frame:文件名，以.npy为扩展名，压缩扩展名为.npz
a = np.arange(100).reshape(5,10,2)
np.save("test.npy",a)
b = np.load("test.npy")
print(b)
