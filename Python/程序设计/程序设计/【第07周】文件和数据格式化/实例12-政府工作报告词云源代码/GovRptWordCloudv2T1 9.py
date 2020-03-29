#GovRptWordCloudv2T1.py
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import wordcloud
#from scipy.misc import imread
import imageio
mask = imageio.imread("fivestart.png")
excludes = { }
f = open("新时代中国特色社会主义.txt", "r", encoding="UTF-8")
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
w.to_file("grwordcloud.png")

plt.im = Image.open("grwordcloud.png")
plt.im.show()
