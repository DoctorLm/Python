'''
    -文件的使用方式：打开-操作-关闭
    -文本文件&二进制文件，open() close()
    -文件内容的读取：read() .readline .readlines()
    -数据的文件写入：write() .writelines() .seek()
'''
'''
                      向文件写入一个字符串或字节流
         <f>.write(s) >>>f.write("中国是一个伟大的国家!")
                      将一个元素全为字符串的列表写入文件
<f>.writelines(lines) >>>ls = ["中国","法国","英国"]
                      >>>f.writelines(ls)
                      中国法国美国
                      0-文件开头;1-当前位置;2-文件结尾
    <f>.seek(offset) >>>f.seek(0) #回到文件开头
'''

fo = open("output.txt", "w+")
ls = ["中国","法国","英国"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
