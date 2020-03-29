import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/System/Library/Fonts/Hiragino Sans GB.ttc", size=10)
plt.title('中文标题',fontproperties=font)
plt.show()

#/usr/share/fonts/truetype/arphic/uming.ttc linux
#/System/Library/Fonts/Hiragino Sans GB.ttc windows
