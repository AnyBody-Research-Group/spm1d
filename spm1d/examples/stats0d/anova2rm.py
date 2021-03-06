from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import spm1d




#(0) Load dataset:
dataset    = spm1d.data.uv0d.anova2rm.Antidepressant()
# dataset    = spm1d.data.uv0d.anova2rm.RSXLTraining()
# dataset    = spm1d.data.uv0d.anova2rm.SocialNetworks()
# dataset    = spm1d.data.uv0d.anova2rm.Southampton2rm()
# dataset    = spm1d.data.uv0d.anova2rm.SPM1D3x3()
# dataset    = spm1d.data.uv0d.anova2rm.SPM1D3x4()
# dataset    = spm1d.data.uv0d.anova2rm.SPM1D3x5()
# dataset    = spm1d.data.uv0d.anova2rm.SPM1D4x4()
# dataset    = spm1d.data.uv0d.anova2rm.SPM1D4x5()
y,A,B,SUBJ = dataset.get_data()
print(dataset)





#(1) Run ANOVA:
F = spm1d.stats.anova2rm(y, A, B, SUBJ)
# F = spm1d.stats.anova2rm(y, B, A, SUBJ)
Fvalues = [f.z for f in F]
print(Fvalues)







