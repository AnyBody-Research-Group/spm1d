from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import os
import numpy as np
from .. import _base




class _SPM1D_ANOVA3TWORM_DATASET(_base.DatasetANOVA3rm, _base.Dataset1D):
	def _set_values(self):
		self._set_datafile()
		Z             = np.load(self.datafile)
		self.Y,self.A,self.B,self.C,self.SUBJ = Z['Y'], Z['A'], Z['B'], Z['C'], Z['SUBJ']
		Z.close()


class SPM1D_ANOVA3TWORM_2x2x2(_SPM1D_ANOVA3TWORM_DATASET):
	def _set_datafile(self):
		self.datafile = os.path.join(_base.get_datafilepath(), 'spm1d_anova3tworm_2x2x2.npz')
class SPM1D_ANOVA3TWORM_2x3x4(_SPM1D_ANOVA3TWORM_DATASET):
	def _set_datafile(self):
		self.datafile = os.path.join(_base.get_datafilepath(), 'spm1d_anova3tworm_2x3x4.npz')

