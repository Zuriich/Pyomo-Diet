import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-1.5, 1.5, 101)


pl.figure(figsize = ( 4 , 4 ))

pl.plot(x, np.sqrt(.2 + x**2), linewidth=2)
pl.text(-1, 0, '$f$ (smooth)', size=20)

pl.ylim(ymin=-.2)
pl.axis('off')
pl.tight_layout()

pl.show()
