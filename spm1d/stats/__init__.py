'''
Statistics module.

This module contains functions for conducting classical hypothesis testing on a set of 1D continua.

For all tests the dependent variable **Y** must be a NumPy array, with dimensions::

* J :  number of observations
* Q :  number of field nodes
* I :  number of vector components

Specifically:

* Univariate 0D tests:  **Y** should be ( J x 1 )
* Multivariate 0D tests:  **Y** should be ( J x I )
* Univariate 1D tests:  **Y** should be ( J x Q )
* Multivariate 1D tests:  **Y** should be ( J x Q x I )

'''
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

from . import _spm

from .t import ttest, ttest_paired, ttest2, regress, glm

from .anova import anova1,anova1rm
from .anova import anova2,anova2nested,anova2rm,anova2onerm
from .anova import anova3,anova3nested,anova3rm,anova3tworm,anova3onerm

from .hotellings import hotellings, hotellings_paired, hotellings2
from .cca import cca
from .manova import manova1
