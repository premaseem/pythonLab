"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge
ML - Centraal tendency in data set
"""
import numpy
from scipy import stats

data = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = sum(data)/len(data)
mean_numpy = numpy.mean(data)

median = sorted(data)[len(data)//2]
median_numpy = numpy.median(data)

m={}
for e in data:
    v = m.setdefault(e,0)
    v += 1
    m[e]=v
mode = None
max_freq = 0

for k,v in m.items():
    if v >max_freq:
        max_freq  = v
        mode = k

mode_scipy = stats.mode(data)



