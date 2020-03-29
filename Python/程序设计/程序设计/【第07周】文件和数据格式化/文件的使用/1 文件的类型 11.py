'''
    -文件的使用方式：打开-操作-关闭
    -文本文件&二进制文件，open() close()
    -文件内容的读取：read() .readline .readlines()
    -数据的文件写入：write() .writelines() .seek()
'''

#文本形式打开文件
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()

#二进制形式打开文件
bf = open("f.txt", "rb")
print(bf.readline())
bf.close()
