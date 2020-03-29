'''
函数的定义
函数是一段代码的表示
def <函数名>(<参数(0个或多个)>):
    <函数体>
    return <返回值>
'''
#案列：计算n!
def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

#函数的使用及调用过程
a = fact(10) #函数调用
print(a)

'''
函数的参数传递
可选参数传递
函数定义时可以为某些参数指定默认值，构成可选参数
def <函数名>(<非可选参数>,<可选参数>):
    <函数体>
    return <返回值>
'''
#计算n!//m
def fact1(n,m=1):
    s = 1
    for i in range(1, n+1):
        s*=i
    return s//m

a = fact1(10)
print(a)
a = fact1(10,5) #位置传参fact1(10,5) 名称传参fact1(n = 10,m = 5)
print(a)

'''
函数的参数传递
可变参数传递
函数定义时可以设计可变数量参数，既不确定参数总数量
def <函数名>(<可选参数>, *b ):
    <函数体>
    return <返回值>
'''
#计算n!乘数
def fact2(n, *b):
    s = 1
    for i in range(1, n+1):
        s*=i
    for item in b:
        s*=item
    return s

a = fact2(10)
print(a)
a = fact2(10,3)
print(a)
a = fact2(10,3,5,8)
print(a)

'''函数的返回值
函数可以返回0个金或多个结果
-return保留字用来传递返回值
-函数可以有返回值,也可以没有，可以有return，也可以没有
-return可以传递0个返回值，也可以传递任意多个返回值
'''

def fact3(n,m=1):
    s = 1
    for i in range(1, n+1):
        s*=i
    return s//m, n, m

a = fact3(10) #返回为元组类型
print(a)
a = fact3(10,5)
print(a)
a,b,c = fact3(10,5)
print(a,b,c)

'''
        局部变量和全局变量
        <语句块1>
        def <函数名>(<参数>):
  程序       <函数体>              函数
全局变量      return <返回值>      局部变量
        <语句块2>
'''
n, s = 10, 100      #n和s是全局变量
def fact4(n):
    s = 1           #fact4()函数中的n和s是局部变量
    for i in range(1, n+1):
        s*=i
    return s
print(fact4(n), s)  #n和s是全局变量


n, s = 10, 100      #n和s是全局变量
def fact5(n):
    global s        #函数中使用global保留字 声明此处s是全局变量s
    for i in range(1, n+1):
        s*=i
    return s
print(fact5(n), s)  #n和s是全局变量

#规则2:局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F", "f"]
def func(a):
    ls.append(a)
    return
func("C")
print(ls)

ls = ["F", "f"]
def func1(a):
    ls = []
    ls.append(a)
    return
print(func1("C"))
print(ls)
#使用规则
#基本数据类型，无论是否重名，局部变量与全局变量不同
#可以通过global保留字在函数内部声明全局
#组合数据类型，如果局部变量未真实创建，则是全局变量

'''
    lambda函数
lambda函数返回函数名作为结果
-lambda函数是一种女匿名函数，即没有名字的函数
-使用lambda保留字定义，函数名是返回结果
-lambda函数用于定义简单的、能够在一行内表示的函数
<函数名>=lambda <参数>:<表达式>
'''
f = lambda x,y:x+y
a = f(10,15)
print(a)
f = lambda:"lambda函数"
print(f())
