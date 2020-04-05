import numpy as np

'''ndarray数组的创建方法
从python中的列表、元组等类型创建ndarray数组
 x = np.array(list/tuple)
 x = np.array(list/tuple,dtype=np.float32)
当np.array()不指定dtype时，NumPy将根据数据情况关联一个dtype类型'''
x = np.array([0,1,2,3,4])   #列表类型创建
print(x)
x = np.array([5,6,7,8,9])   #从元组类型创建
print(x)
x = np.array([[1,2],[9,8],(0.1,0.2 )])  #从列表、元组混合类型中创建
print(x)
'''ndarray数组的创建方法
使用Numpy中函数创建ndarray数组,如：arange,ones,zeros等'''
x = np.arange(10)       #类似range()函数，返回ndarray类型，元素从0至n-1
print(x)
x = np.ones((2,3,4))    #根据shape生成一个全1数组,shape是元组类型
print(x)
x = np.zeros((2,3,4))   #根据shape生成一个全0数组,shape是元组类型
print(x)
x = np.full(10,3.14)    #根据shape生成一个数组,每个元素值都是val
print(x)
x = np.eye(5)           #创建一个正方的n*n单位矩阵，对角线为1,其余为0
print(x)

a = np.ones((2,3,4))
x = np.ones_like(a)   #根据数组a的形状生成一个全1数组
print(x)
x = np.zeros_like(a)  #根据数组a的形状生成一个全1数组
print(x)
np.full_like(a,3.14)  #根据数组a的形状生成一个数组，每个元素值都是val
print(x)

a = np.linspace(1,10,4)   #根据起止数据等间距地填充数据，形成数组
b = np.linspace(1,10,4,endpoint=False)
print(a,b)
x = np.concatenate((a,b)) #将两个或多个数组合并成一个新数组
print(x)

a = np.ones((2,3,4),dtype=np.int)

x = a.reshape((3,8))    #改变数组元素，返回一个shape形状的数组，原数组不变
print(x)

x = a.resize((3,8))     #与.reshape()功能一致，但修改原数组
print(x)

x = a.swapaxes(0,1) #将数组n个维度中两个维度进行调换
print(x)

b = a.flatten()     #对数组进行降维，返回折叠后的一维数组，原数组不变
print(b)

a = np.ones((2,3,4),dtype=np.int)
print(a)
new_a = a.astype(np.float) #数组类型变换
print(a,new_a)

a = np.full((2,3,4),25,dtype=np.int)
print(a)
b = a.tolist() #数组向列表的转换
print(b)
