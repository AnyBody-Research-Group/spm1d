from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *

from matplotlib import pyplot
import spm1d



#(0) Load dataset:
dataset      = spm1d.data.uv1d.anova1.SpeedGRFcategorical()
dataset      = spm1d.data.uv1d.anova1.Weather()
Y,A          = dataset.get_data()



#(1) Run ANOVA:
alpha        = 0.05
F            = spm1d.stats.anova1(Y, A, equal_var=False)
Fi           = F.inference(alpha, interp=False)
print(Fi)
### alternative syntax:
# Y0,Y1,Y2     = [Y[A==u] for u in np.unique(A)]
# F            = spm1d.stats.anova1((Y0,Y1,Y2), equal_var=False)


#(2) Plot results:
pyplot.close('all')
Fi.plot()
Fi.plot_threshold_label(bbox=dict(facecolor='w'))
# pyplot.ylim(-1, 500)
pyplot.xlabel('Time (%)', size=20)
pyplot.title(r'Critical threshold at $\alpha$=%.2f:  $F^*$=%.3f' %(alpha, Fi.zstar))
pyplot.show()





