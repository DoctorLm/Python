import matplotlib.pyplot as plt
import matplotlib

'用于显示字体名字'
matplotlib.rcParams['font.family']='Songti SC'

' 字体风格，正常 normal 或 italic '
matplotlib.rcParams['font.style']='normal'
'字体大小，整数字号或large、x-small'
matplotlib.rcParams['font.size']='13'
plt.plot([3,1,4,5,2])
plt.plot("纵轴(值)")
#plt.savefig('test',dpi=600)
plt.show()


