import numpy
from mayavi import mlab

s = numpy.random.random((10, 10))
img = mlab.imshow(s, colormap='gist_earth')
mlab.show()
