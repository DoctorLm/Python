import numpy as np
import matplotlib.pyplot as plt
#'plt.plot(x,y,format_string,**kwargs)'
#format_string:控制曲线的格式字符串,可选由颜色字符、风格字符和标记字符组成
#颜色字符    说明         颜色字符        说明
#'b'        蓝色           'm'         洋红色magenta
#'g'        绿色           'y'         黄色
#'r'        红色           'k'         黑色
#'c'        青绿色cyan     'W'         白色
#'#008000'  RGB某颜色      '0.8'       灰度值字符串
#风格字符
#'-'    实线
#'--'   破折线
#'-.'   点划线
#':'    虚线
#'' ''  无线条
#标记字符   说明
#'.'      点标记
#','      像素标记（极小点）
#'o'      实心圈标记
#'v'      倒三角标记
#'^'      上三角标记
#'>'      右三角标记
#'<'      左三角标记
#'1'      下花三角标记
#'2'      上花三角标记
#'3'      左花三角标记
#'4'      右花三角标记
#'s'      实心方形标记
#'P'      实心五角标记
#'*'      星形标记
#'h'      竖六边形标记
#'H'      横六边形标记
#'+'      十字标记
#'x'      x标记
#'D'      菱形标记
#'d'      瘦菱形标记
#'|'      垂直线标记
#**kwargs:第二组或更多（x,y,format_string）
#color:控制颜色，clor='grenn'
#linestyle:线条风格,linestyle='dashed'
#marker:标记风格，marker='o'
#markerfacecolor:标记颜色，markerfacecolor='blue'
#markersize:标记尺寸，markersize=20

plt.subplot(211)
a = np.arange(10)
plt.plot(a,a*1.5,'r-', a,a*2.5,'r--', a,a*3.5,'-.', a,a*4.5,':')

plt.subplot(212)
a = np.arange(10)
plt.plot(a,a*1.5,'go-', a,a*2.5,'rx', a,a*3.5,'*', a,a*4.5,'b-.')

plt.show()
