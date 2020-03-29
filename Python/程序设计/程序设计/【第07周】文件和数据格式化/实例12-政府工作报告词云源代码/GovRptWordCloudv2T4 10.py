#GovRptWordCloudv2T4.py
import jieba
import wordcloud
import imageio
mask = imageio.imread("chinamap.jpg")
excludes = { }
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
                        width = 1000, height = 700,\
                        background_color = "white",
                        font_path = "Hiragino Sans GB.ttc", mask = mask
                        )
w.generate(txt)
w.to_file("grwordcloudm.png")
