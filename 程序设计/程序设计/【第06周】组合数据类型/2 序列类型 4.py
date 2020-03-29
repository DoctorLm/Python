#序列类型定义
#序列类型通用操作符
ls = ["python",123,".io"]
print(ls[::-1])
s = "python123.io"
print(s[::-1])

print(len(ls))
print(min(s))
print(max(s))

#元组类型定义
creature = "cat","dog","tiger","human"
print(creature)
color = (0x001100,"blue",creature)
print(color)
print(color[-1][2])

#元组类型操作
creature = "cat","dog","tiger","human"
print(creature[::-1])

#列表类型定义 [] 或 list()
ls = ["cat","dog","tiger",1024]
print(ls)
It = ls
print(It)
ls+=It
print(ls)
print(It)
#列表类型操作
ls = ["cat","dog","tiger",1024]
ls[1:2] = [1,2,3,4]
print(ls)
del ls[::3]
print(ls)
print(ls*2)
