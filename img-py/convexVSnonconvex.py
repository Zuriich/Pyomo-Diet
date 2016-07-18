import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

a = np.linspace( -1 , 2)

pl.figure(figsize = (8 , 4))


pl.subplot(1 , 3 , 1)
pl.plot( a , a ** 2 , linewidth = 2)
pl.text( -.7 , -.6**2, '$f$', size = 20)


pl.plot( [.35 , 1.85], [.35 ** 2 , 1.85 **2 ])
pl.plot( [.35 , 1.85], [.35 ** 2 , 1.85 **2 ], 'k+')
pl.text( .35 - .2 , .35 **2 + .1, 'A', size = 15)
pl.text( 1.85 - .2 , 1.85 ** 2 , 'B', size = 15)


pl.plot( a, 2*a -1 )
pl.plot( 1 , 1, 'k+')
pl.text( .3, -.75 , "Tangent to $f$", size = 15)
pl.text ( 1 , 1 - .5 , 'C', size = 15)

pl.ylim( ymin = -1 )
pl.axis('off')
pl.tight_layout()

pl.text( -1, 3 , "CONVEX", size = 15)


pl.subplot(1 , 3 , 3)
pl.plot( a , a ** 2 + np.exp(-5 * ( a - .5) ** 2) , linewidth = 2)
pl.text( -.7 , -.6**2, '$f$', size = 20)

pl.ylim( ymin = -1 )
pl.axis('off')
pl.tight_layout()

pl.text( -1, 3 , "NON-CONVEX", size = 15)
