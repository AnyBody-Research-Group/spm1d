from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import os
import numpy as np
from matplotlib import pyplot



# load plain-text data (30 rows, 100 columns):
dir0         = os.path.dirname(__file__)
fname        = os.path.join(dir0, 'data', 'ex_kinematics.txt')
Y            = np.loadtxt(fname)   #30 curves, 100 nodes

# plot:
pyplot.close('all')
pyplot.plot(Y.T, color = 'k')
pyplot.xlabel('Time (%)', size=20)
pyplot.ylabel(r'$\theta$ (deg)', size=20)
pyplot.show()
