"""
GIF test
*** Need to install images2gif, Figtodat
From Sukhbinder Singh @
https://sukhbinder.wordpress.com/2014/03/19/gif-animation-in-python-in-3-steps/
"""
import Figtodat
from images2gif import writeGif
import matplotlib.pyplot as plt
import numpy

figure = plt.figure()
plot   = figure.add_subplot (111)

plot.hold(False)
    # draw a cardinal sine plot
images=[]
y = numpy.random.randn(100,5)
for i in range(y.shape[1]):
    plot.plot (numpy.sin(y[:,i]))
    plot.set_ylim(-3.0,3)
    plot.text(90,-2.5,str(i))
    im = Figtodat.fig2img(figure)
    images.append(im)

writeGif("images.gif",images,duration=0.3,dither=0)
