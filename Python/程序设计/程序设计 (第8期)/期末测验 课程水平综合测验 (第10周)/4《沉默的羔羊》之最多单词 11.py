描述

附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬

'''
如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词
输入格式
文件
输出格式
字符串
输入输出示例
仅提供一个输出示范样例。
输入     输出
无       羔羊
解答代码
思路：利用jieba库进行分词，然后主要用到了字典的get方法和列表的sort()方法。不过这题中按照Unicode排序这一步没有做，也通过了测试。评论区有小伙伴给出了解答，所以代码也相应进行了更新。
'''
import jieba
with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        # 过滤长度为1的单词
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
# 对词语根据出现的频率进行排序
wordlst = list(counts.items())
wordlst.sort(key=lambda x:x[1], reverse=True)
maxfreq = wordlst[0][1]  # 确定最大的频率
maxfreqwords = []  # 新建一个最大频率单词的列表(假设存在多个单词频率相同，且频率最大)
for i in wordlst:
    if i[1] == maxfreq:
        maxfreqwords.append(i)
    else:
        break  # 一旦遍历至频率值小于最大频率值时，跳出，不必继续遍历，节约计算时间
maxfreqwords.sort(key=lambda x:x[0], reverse=True)  # 按照Unicode排序
print(maxfreqwords[0][0])

