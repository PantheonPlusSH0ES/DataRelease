import pandas as pd
import numpy as np
from scipy import interpolate

d = pd.read_csv('g_filt_tonry.txt',delim_whitespace=True,names=['L','F'])
l=[0.]
l.extend(d['L'])
l.append(9999999)
f=[0.]
f.extend(d['F'])
f.append(0)
i = interpolate.interp1d(l,f)
d['F'] = i(d['L']+30.)
d.to_csv('g_filt_+30A.txt',index=False,header=False,sep=' ')




d = pd.read_csv('g_filt_tonry.txt',delim_whitespace=True,names=['L','F'])
l=[0.]
l.extend(d['L'])
l.append(9999999)
f=[0.]
f.extend(d['F'])
f.append(0)
i = interpolate.interp1d(l,f)
d['F'] = i(d['L']-30.)
d.to_csv('g_filt_-30A.txt',index=False,header=False,sep=' ')



