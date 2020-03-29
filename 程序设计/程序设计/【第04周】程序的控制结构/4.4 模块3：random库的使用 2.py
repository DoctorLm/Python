import random

#初始化给定的随机数种子，默认为当前系统时间
random.seed(10)

#生成一个【0.0, 10)之间的随机小数
a = random.random()
print(a)

#生成一个[a,b]之间的整数
a = random.randint(10, 100)
print(a)

#生成一个[m,n]之间以K为步长的随机整数
a = random.randrange(10, 100, 10)
print(a)

#生成一个k比特长的随机整数
a = random.getrandbits(16)
print(a)

#生成一个[a,b]之间的随机小数
a = random.uniform(10, 100)
print(a)

#从序列seq中随机选择一个元素
a = random.choice([1,2,3,4,5,6,7,8,9])
print(a)

#将序列seq中随机排序,返回一个打乱后的序列
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a)
