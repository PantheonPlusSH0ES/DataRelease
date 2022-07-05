#! /usr/bin/env python
# S.ROdney
# 2011.04.07
# interpolate HST filter throughput curves to regular 
# wavelength spacing for SNANA

from scipy import interpolate
import sys
from numpy import loadtxt, where, arange, append

from pylab import *

def plotUVIS( ) :
    plot1('WFC3_UVIS_F225W.dat' , ls='--' )
    plot1('WFC3_UVIS_F275W.dat' , ls='--')
    plot1('WFC3_UVIS_F336W.dat' , ls='--')
    plot1('WFC3_UVIS_F350LP.dat', ls='--' )
    plot1('WFC3_UVIS_F390W.dat' , ls='--')

def plotACS( ) :
    plot1('ACS_WFC_F435W.dat' )
    plot1('ACS_WFC_F475W.dat')
    plot1('ACS_WFC_F606W.dat')
    plot1('ACS_WFC_F625W.dat')
    plot1('ACS_WFC_F775W.dat')
    plot1('ACS_WFC_F814W.dat')
    plot1('ACS_WFC_F850LP.dat')

def plotIR( ) :
    plot1('WFC3_IR_F105W.dat')
    plot1('WFC3_IR_F110W.dat')
    plot1('WFC3_IR_F125W.dat')
    plot1('WFC3_IR_F140W.dat')
    plot1('WFC3_IR_F160W.dat')

def plotCLASH( ) : 
    
   
    # plot1('CLASH/HST_ACS_WFC_F435W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F475W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F555W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F606W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F625W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F775W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F814W.res',skiprows=5)
    # plot1('CLASH/HST_ACS_WFC_F850LP.res',skiprows=5)
    # 
    # plot1('CLASH/HST_WFC3_IR_F105W.res',skiprows=5)
    # plot1('CLASH/HST_WFC3_IR_F110W.res',skiprows=5)
    # plot1('CLASH/HST_WFC3_IR_F125W.res',skiprows=5)
    # plot1('CLASH/HST_WFC3_IR_F140W.res',skiprows=5)
    # plot1('CLASH/HST_WFC3_IR_F160W.res',skiprows=5)

    plot1('CLASH/HST_WFC3_UVIS_F218W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F225W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F275W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F300X.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F336W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F390W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F438W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F475W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F555W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F606W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F625W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F775W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F814W.res',skiprows=5)
    plot1('CLASH/HST_WFC3_UVIS_F850LP.res',skiprows=5)


def plot1( filename, skiprows=1, **kwargs ) : 
    w,f = loadtxt( filename, skiprows=skiprows, unpack=True )
    plot(w,f, label=filename.rstrip('.dat'), **kwargs )
    

def main(): 
    import glob
    reslist = glob.glob("HST*res")
    for resfile in reslist : 
        datfile = resfile.lstrip('HST_').replace('.res','.dat')
        interp1( resfile, datfile ) 

def interp1(infile,outfile): 

    # import pdb; pdb.set_trace()
    win,fin = loadtxt( infile, unpack=True )
    wmin = win[ where(fin>0)[0][0]]
    wmax = win[ where(fin>0)[0][-1]]

    # interpolate to 5 angstrom steps
    # tacking on zeros at the top and bottom
    wout = arange( int(wmin)-50, int(wmax)+51, 5 )
    # wout = arange( int(wmin)-50, int(wmax)+51, 10 )

    #wout = arange( int(wmin)-50, int(wmax)+51, 100 )

    interp = interpolate.interp1d( win, fin, kind='linear', bounds_error=False, fill_value=0 )
    fout = interp( wout )

    # write out the results
    output = open( outfile, 'w' )
    for w,f in zip( wout, fout ) :
        print >> output, '%9.1f  %9.3f'%(w,f)
    output.close()

    print( 'Interpolated filter transmission written to %s'%outfile )

if __name__=="__main__":
    main()

    
