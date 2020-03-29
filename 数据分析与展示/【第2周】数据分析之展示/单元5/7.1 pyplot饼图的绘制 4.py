import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Heiti TC'
matplotlib.rcParams['font.size'] = 12

labels = '华为', '苹果', '小米', '格力'
sizes = [45, 15, 30, 10]
explode = (0.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('业绩分析图')
plt.show()


