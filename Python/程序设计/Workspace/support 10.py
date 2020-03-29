#coding:utf8
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
