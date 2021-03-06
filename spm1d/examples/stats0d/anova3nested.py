from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import spm1d




#(0) Load data:
dataset   = spm1d.data.uv0d.anova3nested.SouthamptonNested3()
y,A,B,C   = dataset.get_data()
print(dataset)


#(1) Run ANOVA:
F = spm1d.stats.anova3nested(y, A, B, C)
Fvalues = [f.z for f in F]
DF = [f.df for f in F]
print(Fvalues)
print(DF)


