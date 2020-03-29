'''
    -文件的使用方式：打开-操作-关闭
    -文本文件&二进制文件，open() close()
    -文件内容的读取：read() .readline .readlines()
    -数据的文件写入：write() .writelines() .seek()
    '''

文本形式打开文件
tf = open("f.txt", "rt")
print(tf.read(2))
print(tf.readline())
print(tf.readlines())
tf.close()

#遍历全文本：方法一
fname = input("请输入要打开的文件名称:")
fo = open(fname, "r")
txt = fo.read()
#对txt进行处理
fo.close()

#遍历全文本：方法二
fname = input("请输入要打开的文件名称:")
fo = open(fname, "r")
txt = fo.read(2)
while txt != "":
    #对txt进行金处理
    txt = fo.read(2)
fo.close()

#逐行遍历全文本：方法一
fname = input("请输入要打开的文件名称:")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()

#逐行遍历全文本：方法二
fname = input("请输入要打开的文件名称:")
fo = open(fname, "r")
for line in fo:
    print(line)
fo.close()
