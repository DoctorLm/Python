#字符串类型及操作

#字符串类型表示

a = 'abc'
print(a)
a = "abc"
print(a)
a = '''abc'''
print(a)
a = "abc"
print(a)

TempStr = "请输入带有符号的温度值:"

k = len(TempStr)
while k:
    print("{:3}".format(-k),end=" ")
    k -=1
print()
n = 0
for i in TempStr:
    print("[{:}]".format(i), end="")
print()
for i in TempStr:
    print("{:3}".format(n), end="")
    n += 1;
print()
'''字符串的使用
    使用[ ]获取字符串中一个或多个字符
    - 索引:返回字符串中单个字符 <字符串>[M]
    "请输入带有符号的温度值: "[0] 或者 - 切片:返回字符串中一段字符子串
    "请输入带有符号的温度值: "[1:3] 或者
    TempStr[-1]
    <字符串>[M: N]
    TempStr[0:-1]
    '''
print(TempStr[0],TempStr[-1])
print(TempStr[1:3],TempStr[0:-1])

#字符串切片高级用法
#使用[M: N: K]根据步长对字符串切片
#- <字符串>[M: N]，M缺失表示至开头，N缺失表示至结尾
str = "〇一二三四五六七八九十"
print(str[:3])
#- <字符串>[M: N: K]，根据步长K对字符串切片
print(str[1:8:2])
print(str[::-1])

'''
    字符串的特殊字符
    转义符 \
    - 转义符表达特定字符的本意 "这里有个双引号(\")" 结果为 这里有个双引号(")
    - 转义符形成一些组合，表达一些不可打印的含义
    "\b"回退 "\n"换行(光标移动到下行首) "\r" 回车(光标移动到本行首)
    '''
print(" 这里有个双引号(\")")

'''
    字符串操作符
    由0个或多个字符组成的有序字符序列
    操作符及使用                  描述
    x+y                         连接两个字符串x和y
    n*x 或 x*n                  复制n次字符串x
    x in s                      如果x是s的子串，返回True，否则返回False
    '''
#WeekNamePrintV1.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字(1-7):"))
pos = (weekId - 1) * 3
print(weekStr[pos: pos+3])

#WeekNamePrintV2.py
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字(1-7):"))
print("星期" + weekStr[weekId-1])
'''
    字符串处理函数
    一些以函数形式提供的字符串处理功能
    len(x)              长度，返回字符串x的长度
    len("一二三456") 结果为 6
    str(x)              任意类型x所对应的字符串形式
    str(1.23)结果为"1.23" str([1,2])结果为"[1,2]"
    hex(x) 或 oct(x)    整数x的十六进制或八进制小写形式字符串
    hex(425)结果为"0x1a9" oct(425)结果为"0o651"
    chr(u)              x为Unicode编码，返回其对应的字符
    ord(x)              x为字符，返回其对应的Unicode编码
    '''
print(chr(97),ord("a"))

'''Unicode编码
    Python字符串的编码方式
    - 统一字符编码，即覆盖几乎所有字符的编码方式
    - 从0到1114111 (0x10FFFF)空间，每个编码对应一个字符 - Python字符串中每个字符都是Unicode编码字符
    '''
print("1 + 1 = 2 " + chr(10004))
a = "这个字符♉的Unicode值是:" + chr(ord("♉"))
print(a)
for i in range(12):
    print(chr(9800 + i), end="")

'''
    字符串处理方法
    一些以方法形式提供的字符串处理功能
    str.lower() 或 str.upper()       返回字符串的副本，全部字符小写/大写
    "AbCdEfGh".lower() 结果为 "abcdefgh"
    str.split(sep=None)             返回一个列表，由str根据sep被分隔的部分组成
    "A,B,C".split(",") 结果为 ['A','B','C']
    str.count(sub)                  返回子串sub在str中出现的次数
    "an apple a day".count("a") 结果为 4
    str.replace(old, new)           返回字符串str副本，所有old子串被替换为new
    "python".replace("n","n123.io") 结果为 "python123.io"
    str.center(width[,fillchar])    字符串str根据宽度width居中，fillchar可选
    "python".center(20,"=") 结果为 '=======python======='
    "= python= ".strip(" =np")      str.strip(chars)从str中去掉在其左侧和右侧chars中列出的字符
    结果为 "ytho"
    str.join(iter)                  在iter变量除最后元素外每个元素后增加一个str
    ",".join("12345") 结果为 "1,2,3,4,5" #主要用于字符串分隔等
    '''
'''
    字符串类型的格式化
    格式化是对字符串进行格式表达的方式
    - 字符串格式化使用.format()方法，用法如下: <模板字符串>.format(<逗号分隔的参数>)
    '''
print( "{}:计算机{}的CPU占用率为{}%".format("2018-10-10","C",10) )
'''
    :    <填充>     <对齐>      <宽度>        <,>         <.精度>       <类型>
    引导  用于填充的  < 左对齐    槽设定的输      数字的千位    浮点数小数   整数类型
    符号  单个字符    > 右对齐    出宽度          分隔符      精度 或 字   b, c, d, o, x, X
    ^ 居中对齐                             符串最大输   浮点数类型 e, E, f, %
    '''
print("{0:,.2f}".format(12345.6789))
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
