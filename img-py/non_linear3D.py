import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

A = np.arange( -4 , 4 , 0.25)
B = np.arange( -4 , 4 , 0.25)

A , B = np.meshgrid( A , B)

fig1 = pl.figure()
pl.figure(figsize = ( 8 , 4 ))
ax = Axes3D(fig1)

D = A** 2 + B** 2

ax.plot_surface( A , B , D, rstride = 1 , cstride = 1, cmap = pl.cm.hot)

pl.show()
