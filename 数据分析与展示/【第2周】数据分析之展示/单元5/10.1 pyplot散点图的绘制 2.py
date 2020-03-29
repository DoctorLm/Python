import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots()

ax.plot(10*np.random.randn(100), 'o', 10*np.random.randn(100), 'p')

ax.set_title('Simple Scatter')

plt.show()
