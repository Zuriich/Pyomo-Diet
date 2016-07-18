import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

a = np.linspace( -1 , 2)

pl.figure(figsize = (5 , 4))

pl.plot( a , a ** 2 + np.exp(-5 * ( a - .5) ** 2) , linewidth = 2)
pl.text( -.7 , -.6**2, '$f$', size = 20)

pl.plot(-.25,.15, 'ko')
pl.text(-.25 , -.3, '$Global \: minimum$', size = 15)

pl.plot(0.95,1.3, 'ko')
pl.text(0.95,0.9, '$Local \: minimum$', size = 15)



pl.ylim( ymin = -1 )
pl.axis('off')
pl.tight_layout()

pl.text( -1, 3 , "NON-CONVEX", size = 15)

pl.show()
