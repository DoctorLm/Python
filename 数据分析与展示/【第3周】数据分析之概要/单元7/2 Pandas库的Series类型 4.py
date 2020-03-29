import pandas as pd
import numpy as np

#自动索引
b = pd.Series([9,8,7,6])
print(b)
#用户自定义类型
b = pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b)
#标量创建类型
b = pd.Series(25,index=['a','b','c'])
print(b)
#字典类型创建
b = pd.Series({'a':9,'b':8,'c':7})
print(b)
b = pd.Series({'a':9,'b':8,'c':7},index=['c','a','b','d'])
print(b)

#Series类型的基本操作
b = pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b.index)      #.index获取索引
print(b.values)     #.values获取数据
print(b['b'], b[1])
print(b[['c','d',0]])
print(b[['c','d','a']])
print(b[3])
print(b[:3])
print(b[b>b.median()])
print(np.exp(b))


print('c' in b)
print(0 in b)

print(b.get('f',100))

#Series + Series 类型对齐操作
a = pd.Series([1,2,3],index=['c','d','e'])
b = pd.Series([9,8,7,6],index=['a','b','c','d'])
print(a+b)

#Series 类型的name属性
b = pd.Series([9,8,7,6],index=['a','b','c','d'])

b.name = 'Series对象'
b.index.name = '索引列'
print(b)
b.name = 'New对象'
b['b','c'] = 20
print(b)
