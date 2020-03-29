import numpy as np

a = np.array([[0,1,2,3,4],[9,8,7,6,5]])

print(a.ndim)     #秩,即轴的数量或维度数
print(a.shape)    #ndarray对象的尺度，对于矩阵，n行m列
print(a.size)     #ndarray对象的元素个数，相当于.shape中n*m的值
print(a.dtype)    #ndarray对象的元素类型
print(a.itemsize) #ndarray对象中每个元素的大小，以字节为单位
