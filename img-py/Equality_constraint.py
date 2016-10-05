import numpy as np
import pylab as pl

x, y = np.mgrid[-2.9:5.8:.05, -2.5:5:.05]
x = x.T
y = y.T

pl.figure(figsize=(5, 5))
pl.subplot(1 , 2 , 1)
pl.clf()
pl.axes([0, 0, 1, 1])

contours = pl.contour(np.sqrt((x - 3)**2 + (y - 2)**2),
                        extent=[-3, 6, -2.5, 5],
                        cmap=pl.cm.gnuplot)
pl.clabel(contours,
            inline=1,
            fmt='%1.1f',
            fontsize=14)

pl.plot([-3, 6],
            [1.5, - 1.5], 'k', linewidth=2)

pl.plot( 3 , 2 , 'ko')
pl.text( 3 -.2 , 2 + .3, '$Global minimum$', size = 15)

pl.plot( 2.3 , -0.29 , 'ro')
pl.text( 2.3 + .2 , -0.29 , '$Optimum$', size = 15)
pl.text( 6.1 , - 1.6, '$h(x) = 0 $', size = 15)


pl.axvline(0, color='k')
pl.axhline(0, color='k')

pl.text(-.9, 4.4, '$x_2$', size=20)
pl.text(5.6, -.6, '$x_1$', size=20)
pl.title('$ h(x_i) = 0 $', size=20)
pl.axis('equal')
pl.axis('off')
pl.show()
