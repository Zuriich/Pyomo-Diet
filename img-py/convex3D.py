import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
pl.figure(figsize = ( 8 , 4 ))
ax = Axes3D(fig)

A = np.arange( -4 , 4 , 0.25)
B = np.arange( -4 , 4 , 0.25)

A , B = np.meshgrid( A , B)

C = A ** 4 + B ** 4

ax.plot_surface( A , B , C, rstride = 1 , cstride = 1, cmap = pl.cm.hot)

pl.show()
