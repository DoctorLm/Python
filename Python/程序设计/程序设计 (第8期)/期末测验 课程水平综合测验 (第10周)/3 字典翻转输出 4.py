'''描述
读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
即，读入字典key:value模式，输出value:key模式。
输入格式
用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。
输出格式
给定字典d，按照print(d)方式输出。
输入输出示例
用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。
输入    输出
｛‘a’:1, ‘b’:2}    {1:‘a’, 2:‘b’}
解答代码
思路：主要用try…except来控制输入，通过isinstance()方法判断是否是字典，通过zip()来实现key和value互换，注意存在value不可hash的情况，所以需要try…except来监控处理。感谢评论区的小伙伴给出了更简洁的答案。
'''
# 通过测试的版本，这个版本虽然可以通过测试，但是是有问题的，比如输入'abc’就会导致程序报错
s = input()
dict_1 = eval(s)
if isinstance(dict_1, dict):
    dict_2 = dict(zip(dict_1.values(), dict_1.keys()))
    print(dict_2)
else:
    print('输入错误')

# 更推荐这个版本
s = input()
try:
    dict_1 = eval(s)
    if isinstance(dict_1, dict):
        dict_2 = dict(zip(dict_1.values(), dict_1.keys()))
        print(dict_2)
    else:
        print('输入错误')
except:
    print('输入错误')

# 更简洁的答案
s = input()
try:
    dict_1 = eval(s)
    dict_2 = dict(zip(dict_1.values(), dict_1.keys()))
    print(dict_2)
except:
    print('输入错误')

