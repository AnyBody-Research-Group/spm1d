from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from builtins import range

import numpy as np
from .. import _base




class SPM1D2x2x2(_base.DatasetANOVA3rm):
	def _set_values(self):
		nA,nB,nC,nS  = 2,2,2,5
		self.A       = np.hstack([[i]*nB*nC*nS  for i in range(nA)])
		self.B       = np.array(np.hstack([[i]*nC*nS  for i in range(nB)]).tolist() * nA)
		self.C       = np.array(np.hstack([[i]*nS  for i in range(nC)]).tolist() * nA*nB)
		self.SUBJ    = np.hstack([ np.arange(nS)  for i in range(nA*nB*nC)])
		self.Y       = np.array([99, 13, 51, 98,  0, 59, 39, 33, 22, 61, 55, 30, 11, 34, 28, 31, 70, 57, 33, 42, 94, 34, 61, 57, 29, 19, 91, 62, 39, 50, 48, 60, 38,  5, 15, 10,  7, 97, 74, 69])
		#results computed using R (r-project.org):  aov(Y ~ A*B*C + Error(SUBJ/(A*B*C)))
		self.z       = 0.393,2.286,0.136,  0.050,0.083,0.958,  0.010
		self.df      = (1,4),(1,4),(1,4), (1,4),(1,4),(1,4), (1,4)
		self.p       = 0.565,0.205,0.731,  0.834,0.788,0.383,  0.924
		self._atol   = 0.005


class SPM1D2x3x5(_base.DatasetANOVA3rm):
	def _set_values(self):
		nA,nB,nC,nS  = 2,3,5,12
		self.A       = np.hstack([[i]*nB*nC*nS  for i in range(nA)])
		self.B       = np.array(np.hstack([[i]*nC*nS  for i in range(nB)]).tolist() * nA)
		self.C       = np.array(np.hstack([[i]*nS  for i in range(nC)]).tolist() * nA*nB)
		self.SUBJ    = np.hstack([ np.arange(nS)  for i in range(nA*nB*nC)])
		self.Y       = np.array([10, 47,  1, 33, 74, 24,  3, 15,  6, 88, 72, 61, 47, 88,  8,  3,  2,
       76, 90, 67, 89, 25, 67, 28, 35, 89, 68, 95, 45, 61, 64, 55, 12, 31,
       93, 21, 64,  0, 84, 81, 77,  0, 84, 11, 86,  1, 92,  7, 24, 26, 27,
       79, 29, 10, 99, 18, 55, 42, 41, 62, 53, 58, 60,  0, 36, 55, 16, 12,
       84,  8, 94, 68, 58,  6, 47, 58, 93, 84, 22, 82, 35, 61, 61, 75, 46,
       10, 32, 95, 15, 48, 24, 35, 40, 71, 35, 88, 33, 52, 64, 56, 73, 80,
       62, 65, 20, 90, 50, 12, 73, 13, 35, 80, 10, 34, 34, 32, 27, 87, 95,
       77, 72, 79, 63, 66, 33, 48, 50, 28, 73, 74, 85, 18, 75, 82,  0, 19,
       38, 39, 99, 96, 55,  9, 34, 53, 22, 69, 16, 57, 55, 24, 18, 72, 18,
       68, 59, 20, 38, 58, 21, 29,  3,  6, 52, 91, 57, 58, 89, 67, 30, 19,
        5,  1, 62, 14, 45, 63, 77, 12, 55, 56, 55,  8, 10, 42, 65, 29, 21,
       59, 72, 29, 42, 91, 59, 23, 28, 17,  4, 34,  7,  0, 61, 95, 31, 51,
       11, 87, 14, 73, 30, 54, 62, 67, 62, 59,  9, 89, 52, 14, 99, 23, 71,
        4, 88, 56, 44, 58, 93, 43,  3, 12, 86, 21, 49, 63, 14, 90, 18, 92,
       53, 76, 21, 78, 15,  6, 20, 41, 25, 88, 57, 71, 94, 52, 45, 51, 30,
       98, 18, 83, 55, 48, 78, 53, 73, 96, 60, 18, 70, 75, 89, 95, 20, 26,
       47, 15, 93, 46,  5, 49, 55, 88, 36, 33, 67, 30, 12,  9, 61, 42, 87,
       95, 86, 15, 90, 53, 54, 72, 20, 14, 80, 55, 18, 70, 54, 37, 93, 92,
        0,  8, 21, 60,  0, 69, 77, 48, 33, 56, 89,  7, 19, 44, 89, 74, 39,
        0, 81, 56, 54, 33, 86, 86,  5,  0, 68,  0, 34, 81, 31, 95, 56, 56,
       32,  1, 99, 64, 38, 81, 87, 42, 73, 11,  7, 75, 70,  8, 92,  6, 63,
       25, 58, 91])
		#results computed using R (r-project.org):  aov(Y ~ A*B*C + Error(SUBJ/(A*B*C)))
		self.z       = 0.387,1.195,0.272,   0.064,0.695,0.880,  0.75
		self.df      = (1,11),(2,22),(4,44),  (2,22),(4,44),(8,88),  (8,88)
		self.p       = 0.547,0.322,0.895,  0.938,0.600,0.537,  0.648
		self._atol   = 0.005




class SPM1D3x3x3(_base.DatasetANOVA3rm):
	def _set_values(self):
		nA,nB,nC,nS  = 3,3,3,8
		self.A       = np.hstack([[i]*nB*nC*nS  for i in range(nA)])
		self.B       = np.array(np.hstack([[i]*nC*nS  for i in range(nB)]).tolist() * nA)
		self.C       = np.array(np.hstack([[i]*nS  for i in range(nC)]).tolist() * nA*nB)
		self.SUBJ    = np.hstack([ np.arange(nS)  for i in range(nA*nB*nC)])
		self.Y       = np.array([79, 50, 47, 56, 89, 84, 97, 94, 25, 22,  4, 88, 56, 84, 97, 97, 77,
       76,  7, 93, 15,  7,  0, 58, 24, 61, 64, 37, 48, 76, 56, 79, 22, 92,
       73, 49, 93, 78, 12, 85, 98, 62, 15, 21, 61, 35, 44, 53, 23, 61, 57,
       13, 55, 95, 46, 39, 39, 10, 58,  6,  0, 22,  8, 37, 91, 90, 94, 12,
        8,  7,  7, 59, 66, 90, 83, 12, 96, 12, 31, 16, 57, 46, 16, 40, 17,
       77, 27, 37, 70, 26, 88, 47, 30, 80, 22, 85, 76, 77, 81, 26, 70, 18,
       84, 25, 73, 39, 65, 68, 96, 88, 56, 27, 60, 48, 65, 52,  0, 42, 42,
       53, 40, 67,  3, 98, 46,  4, 37, 83,  6, 43, 79, 84, 53, 31, 51, 30,
       59, 33, 47, 94, 83, 27, 92, 55, 63, 61,  8, 54, 20, 51, 99, 64, 61,
       89, 58, 74, 63, 21, 74, 31, 27, 62, 89, 88, 88, 51,  6, 55, 36, 96,
       22, 11, 36, 90,  7, 32,  2, 42, 87, 62, 60, 40, 69, 94, 61, 43, 34,
       31, 60,  3, 95, 45,  1, 21, 12, 26, 63, 77, 56, 50, 63, 57, 55, 55,
       71, 60, 50, 29, 54, 74, 13, 86, 57, 71, 71, 70])
		#results computed using R (r-project.org):  aov(Y ~ A*B*C + Error(SUBJ/(A*B*C)))
		self.z       = 0.042,3.394,0.000,  1.048,1.379,2.123,  0.666
		self.df      = (2,14),(2,14),(2,14),  (4,28),(4,28),(4,28),  (8,56)
		self.p       = 0.959,0.0628,1.000,   0.401,0.266,0.104,  0.719
		self._atol   = 0.005


 