from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import spm1d







#(0) Load dataset:
dataset = spm1d.data.uv0d.anova1.Cars()
# dataset = spm1d.data.uv0d.anova1.Sound()
# dataset = spm1d.data.uv0d.anova1.Southampton1()
# dataset = spm1d.data.uv0d.anova1.ConstructionUnequalSampleSizes()
# dataset = spm1d.data.uv0d.anova1.RSUnequalSampleSizes()
y,A     = dataset.get_data()
print(dataset)



#(1) Run ANOVA
F = spm1d.stats.anova1(y, A, equal_var=True)
print(F)



