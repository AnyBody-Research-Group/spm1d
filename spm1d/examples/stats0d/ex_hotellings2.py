from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

import spm1d




#(0) Load dataset:
dataset = spm1d.data.mv0d.hotellings2.RSXLHotellings2()
# dataset = spm1d.data.mv0d.hotellings2.HELPHomeless()
yA,yB   = dataset.get_data()
print(dataset)



#(1) Conduct T2 test using spm1d:
T2      = spm1d.stats.hotellings2(yA, yB)
T2i     = T2.inference(alpha=0.05)
print(T2i)



