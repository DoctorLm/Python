import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

a = np.array(Image.open("beijing.jpg"))
print(a.shape,a.dtype)

b = [255, 255, 255] -a
plt.im = Image.fromarray(b.astype('uint8'))
im.save("test.jpg")
plt.im.show()
