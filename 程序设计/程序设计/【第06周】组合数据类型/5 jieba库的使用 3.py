import jieba
a = jieba.lcut("中国是一个伟大的国家")
print(a)
a = jieba.lcut("中国是一个伟大的国家",cut_all=True)
print(a)
a = jieba.lcut_for_search("中华人民共和国是伟大的")
print(a)
