import numpy as np
import pylab as pl

pl.figure(1, figsize=(5, 5))
pl.clf()
pl.axes([0, 0, 1, 1])

pl.plot([-1.5, -1.5,  1.5,  1.5, -1.5],
            [-1.5,  1.5,  1.5, -1.5, -1.5], 'k', linewidth=2)

pl.plot([- 1.5,    0,  1.5,  1.5, 0 ,-1 , - 1.5 , - 1.5],
        [   -1,  1.5,  1.5, -  0, 0 ,-1.5, - 1.5 , - 1], 'b', linewidth=2)

pl.fill_between([ -1.5,  1.5],
                    [ -1.5, -1.5],
                    [  1.5,  1.5],
                    color='.8')

pl.fill_between([ -1.5,  0],
                    [ -1, 1.5],
                    [  1.5,  1.5],
                    color='.9')

pl.fill_between([ -1,  0],
                    [ -1.5, 0],
                    [  -1.5,  -1.5],
                    color='.9')

pl.fill_between([ 0,  1.5],
                    [ 0, 0],
                    [  -1.5,  -1.5],
                    color='.9')

pl.text( 0, 1, 'Non Convex Region', size = 15)
pl.text( -1, 1.3, '$Constraint$', size = 15)
pl.text( -.6, -1.3, '$Constraint$', size = 15)

pl.plot( [-1 , 1], [-1, .5], 'r')
pl.plot( [-1 , 1], [-1 , .5], 'k+')
pl.text( -1 - .2 , -1 + .1, 'A', size = 15)
pl.text( 1 - .2 , .5 , 'B', size = 15)

pl.axis('equal')
pl.axis('off')
pl.show()
