from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from builtins import range

import numpy as np
from matplotlib import pyplot
import spm1d






#first-level SPM analysis: (within-subject effects)
nSubj         = 10
BETA          = []  #regression slopes
for subj in range(nSubj):
	dataset   = spm1d.data.uv1d.regress.SpeedGRF(subj=subj)
	Y,x       = dataset.get_data()
	t         = spm1d.stats.regress(Y, x) #conduct linear regression
	BETA.append( t.beta[0] )  #retrieve the regression slope
BETA          = np.array(BETA)


#plot:
pyplot.close('all')
ax            = pyplot.axes( (0.15, 0.15, 0.8, 0.8) )
pyplot.plot(BETA.T, color='k')
ax.axhline(y=0, color='k', linewidth=1, linestyle=':')
ax.set_xlabel('Time (% stance)')
ax.set_ylabel(r'$\beta_0$   $(BW / ms^{-1})$')
pyplot.show()

