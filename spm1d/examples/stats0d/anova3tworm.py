from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import spm1d







#(0) Load dataset:
dataset      = spm1d.data.uv0d.anova3tworm.NYUHiringExperience()
dataset      = spm1d.data.uv0d.anova3tworm.Southampton3tworm()
y,A,B,C,SUBJ = dataset.get_data()
print(dataset)




#(1) Run ANOVA:
F = spm1d.stats.anova3tworm(y, A, B, C, SUBJ, equal_var=True)
Fvalues = [f.z for f in F]
DF = [f.df for f in F]
print(Fvalues)
print(DF)

