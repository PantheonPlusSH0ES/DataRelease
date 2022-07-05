import pandas as pd
import numpy as np
from glob import glob
import os

fs = list(glob('*.dat'))
fs.extend(glob('*.txt'))

for f in fs:
    ls = open(f).readlines()
    fout = open(f,'w')
    for l in ls:
        l,t = float(l.split()[0].strip()),float(l.split()[1].strip())
        if t < .01:
            t = 0
        if 'SDSS.rp.txt' in f:
            t /= 10
            l *= 10
        fout.write('%.6f %.6f\n'%(l,t))
    fout.close()
