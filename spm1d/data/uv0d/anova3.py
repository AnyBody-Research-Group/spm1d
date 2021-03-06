from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import numpy as np
from .. import _base




class RSItalian(_base.DatasetANOVA3):
	def _set_values(self):
		self.www   = 'http://www.real-statistics.com/two-way-anova/anova-more-than-two-factors/'
		self.Y     = np.array([23,18,26,32,13,31,26,34,17,23,28,26,
		                       24,25,14,17,30,18,11,16,25,18,14,25,
							   16,31,17,11,34,24,24,19,31,16,11,19,
							   31,29,40,31,35,25,18,29,36,42,40,36,
						       19,28,31,23,19,14, 4,29,18,22,18,24,
						       29,25,17,12,26,35,10,23,26,18,24,16,
						       28,37,22,44,37,42,30,37,25,38,41,28,
						       35,23,24,11,23,30,26,16,23,14,19,25])
		self.A     = np.array( [0]*12*4 + [1]*12*4 )       #gender
		self.B     = np.array( ([0]*12*2 + [1]*12*2)*2  )  #country
		self.C     = np.array( ([0]*12 + [1]*12)*4  )      #position
		self.z     = 0.01749,16.8113,0.51854, 0.70169,9.2541,0.47708, 26.6077
		self.df    = [(1,88)]*7
		self.p     = 0.89508, 9.2e-5, 0.47337, 0.40449, 0.0031, 0.49157, 1.5e-6
		


class SouthamptonFullyCrossedMixed(_base.DatasetANOVA3):
	def _set_values(self):
		self.www     = 'http://www.southampton.ac.uk/~cpd/anovas/datasets/Doncaster&Davey%20-%20Model%203_2%20Three%20factor%20fully%20cross%20factored.txt'
		self.A       = np.array([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])
		self.B       = np.array([1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2])
		self.C       = np.array([1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2])
		self.Y       = np.array([-3.8558, 4.4076, -4.1752, 1.4913, 5.9699, 5.2141, 9.1467, 5.8209, 9.4082, 6.0296, 15.3014, 12.1900, 6.9754, 14.3012, 10.4266, 2.3707, 19.1834, 18.3855, 23.3385, 21.9134, 16.4482, 11.6765, 17.9727, 15.1760])
		# self.random  = [[False,False,False], [False,True,False], [False,True,True], [True,True,True]]
		# self.z       = [(38.12,0.02,0.99, 7.06,0.42,0.92, 2.06), (5.40,0.00,1.08, 3.43,0.21,0.45, 2.06), (7.03,0.00,-1, 3.43,0.21,0.45, 2.06), (7.03,0.00,-1, 3.43,0.21,0.45, 2.06)]
		self.z       = 38.12,0.02,0.99,  7.06,0.42,0.92,  2.06
		self.df      = (2,12),(1,12),(1,12), (2,12),(2,12),(1,12), (2,12)
		self.p       = '<0.001', 0.902, 0.338,    0.009, 0.665, 0.357,    0.171
		self._atol   = 0.01





