#GovRptWordCloudv1.py
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import wordcloud

f = open("新时代中国特色社会主义.txt", "r", encoding="UTF-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width = 800, height = 600, background_color = "white", font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc")
w.generate(txt)
w.to_file("grwordcloud.png")

plt.im = Image.open("grwordcloud.png")
plt.im.show()
