#TempConvert.py
TempStr = input("请输入带有符号的温度值: ")
k = len(TempStr)
while k:
    print("{:2}".format(-k),end=" ")
    k -=1
print()
for i in TempStr:
    print("[{:}]".format(i), end=" ")
print()
n = 0
for i in TempStr:
    print("{:2}".format(n), end="  ")
    n += 1;
print()

if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
