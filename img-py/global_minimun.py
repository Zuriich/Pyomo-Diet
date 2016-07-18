import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

a = np.linspace( -1 , 2)

pl.figure(figsize = (5 , 4))

pl.plot( a , a ** 2 , linewidth = 2)
pl.text( -.7 , -.6**2, '$f$', size = 20)



pl.plot( 0 , 0 , 'ko')
pl.text( .35 - .2 , -.5, '$Global \: minimun$', size = 15)


pl.ylim( ymin = -1 )
pl.axis('off')
pl.tight_layout()


pl.show()
