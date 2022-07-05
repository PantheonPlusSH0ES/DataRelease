import numpy as np

files=['U_UVOT','B_UVOT','V_UVOT']
for f in files:
    file1=open(f+'.txt','r').readlines()
    file2=open(f+'_rev.txt','w')
    for x in file1:
        x2=x.split()
        file2.write(str(x2[0])+' '+str(float(x2[1])/100.0)+'\n')
#file1.close()
file2.close()
