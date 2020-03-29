#集合类型的定义
A = {"python",123,("python",123)} #使用set()建立集合
B = set("pypy123") #使用set()建立集合
C = {"python",123,"python",123}
print("A:{} B:{} C:{}",A,B,C)
#集合操作符
A = {"p","y",123}
B = set("pypy123")
print("差：",A-B) #差
print("交：",A&B) #交
print("补：",A^B) #补
print("并：",A|B) #并
#集合的处理方法
A = {"p","y",123}
for item in A:
    print(item,end="")
print()
try:
    while True:
        print(A.pop(),end="")
except:
    pass
print("\n",A)
#集合类型及操作
print("包含关系比较")
print('''"p" in {"p","y",123}''',"p" in {"p","y",123})
print('''{"p","y"} >= {"p","y",123}''',{"p","y"} >= {"p","y",123})
#集合类型应用场景
ls = ["p","p","y","y",123]
s = set(ls) #利用集合无重复元素的特点
print(s)
lt = list(s) #将集合转换列表
print(lt)
