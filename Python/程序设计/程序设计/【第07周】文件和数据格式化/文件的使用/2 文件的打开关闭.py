'''
    -文件的使用方式：打开-操作-关闭
    -文本文件&二进制文件，open() close()
    -文件内容的读取：read() .readline .readlines()
    -数据的文件写入：write() .writelines() .seek()
'''

'''
f = open("f.txt")        -文本形式、只读模式、默认值
f = open("f.txt", "rt")  -文本形式、只读械、同默认值
f = open("f.txt", "w")   -文本形式、覆盖写模式
f = open("f.txt", "a+")  -文本形式、追加写模式+读文件
f = open("f.txt", "x")   -文本形式、创建写模式
f = open("f.txt", "b")   -二进制形式、覆盖写模式
'''

#文本形式打开文件
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()

#二进制形式打开文件
bf = open("f.txt", "rb")
print(bf.readline())
bf.close()
