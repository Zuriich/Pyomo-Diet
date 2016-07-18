import numpy as np
import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

a = np.linspace( -1.5 , 1.5 , 101 )

pl.figure(figsize = ( 8 , 4 ))


pl.subplot( 1 , 2 , 1)

pl.plot( a , (2 * a + 3) , linewidth = 2 )
pl.text( 1, 0 , '$Linear$', size = 20 )

pl.ylim ( ymin = -2 )
pl.axis ('off')


pl.subplot( 1 , 2 , 2)

pl.plot( a , (2 * (a**2) + 3) , linewidth = 2 )
pl.text( 1, 0.5 , '$Non-Linear$', size = 20 )

pl.ylim ( ymin = -2 )
pl.axis ('off')
pl.tight_layout()

pl.show()
