from __future__ import print_function

from matplotlib import pyplot
import spm1d



#(0) Load data:
dataset      = spm1d.data.mv1d.hotellings2.Besier2009muscleforces()
YA,YB        = dataset.get_data()  #A:slow, B:fast
print(dataset)



#(1) Conduct test:
alpha        = 0.05
T2           = spm1d.stats.hotellings2(YA, YB)
T2i          = T2.inference(0.05)



#(2) Plot:
pyplot.close('all')
T2i.plot()
pyplot.show()


