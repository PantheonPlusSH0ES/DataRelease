"""
The likelihood module for Pantheon+ SNe combined with SH0ES Cepheids

"""

from cosmosis.gaussian_likelihood import GaussianLikelihood
from cosmosis.datablock import names
import os
import numpy as np
import pandas as pd

# Default is to use SN data from https://arxiv.org/abs/2202.04077
# and Cepheids data from https://arxiv.org/abs/2112.04510
default_data_file = os.path.join(os.path.split(__file__)[0], "Pantheon+SH0ES.dat")
default_covmat_file = os.path.join(os.path.split(__file__)[0], "Pantheon+SH0ES_STAT+SYS.cov")


class PantheonLikelihood(GaussianLikelihood):
    x_section = names.distances
    x_name = "z"
    y_section = names.distances
    y_name = "D_A"
    like_name = "pantheon"

    def build_data(self):
        """
        Run once at the start to load in the data vectors.

        Returns x, y where x is the independent variable (redshift in this case)
        and y is the Gaussian-distribured measured variable (magnitude in this case).

        """
        filename = self.options.get_string("data_file", default=default_data_file)
        print("Loading data from {}".format(filename))
        data = pd.read_csv(filename,delim_whitespace=True)
        self.origlen = len(data)
        
        self.ww = (data['zHD']>0.01)

        self.zCMB = data['zHD'][self.ww] #use the vpec corrected redshift for zCMB 
        self.zHEL = data['zHEL'][self.ww]
        self.m_obs = data['m_b_corr'][self.ww]

        return self.zCMB, self.m_obs

    def build_covariance(self):
        """Run once at the start to build the covariance matrix for the data"""
        filename = self.options.get_string("covmat_file", default=default_covmat_file)
        print("Loading covariance from {}".format(filename))

        # The file format for the covariance has the first line as an integer
        # indicating the number of covariance elements, and the the subsequent
        # lines being the elements.
        # This function reads in the file and the nasty for loops trim down the covariance
        # to match the only rows of data that are used for cosmology

        f = open(filename)
        line = f.readline()
        n = int(len(self.zCMB))
        C = np.zeros((n,n))
        ii = -1
        jj = -1
        mine = 999
        maxe = -999
        for i in range(self.origlen):
            jj = -1
            if self.ww[i]:
                ii += 1
            for j in range(self.origlen):
                if self.ww[j]:
                    jj += 1
                val = float(f.readline())
                if self.ww[i]:
                    if self.ww[j]:
                        C[ii,jj] = val
        f.close()

        print('Done')

        # Return the covariance; the parent class knows to invert this
        # later to get the precision matrix that we need for the likelihood.
        return C

    def extract_theory_points(self, block):
        """
        Run once per parameter set to extract the mean vector that our
        data points are compared to.  For the Hubble flow set, we compare to the 
        cosmological model. For the calibrators we compare to the Cepheid distances.
        """
        import scipy.interpolate

        # Pull out theory mu and z from the block.
        theory_x = block[self.x_section, self.x_name]
        theory_y = block[self.y_section, self.y_name]
        theory_ynew = self.zCMB*np.nan

        # Interpolation function of theory so we can evaluate at redshifts of the data
        f = scipy.interpolate.interp1d(theory_x, theory_y, kind=self.kind)
        
        # Actually do the interpolation at the data redshifts
        zcmb = self.zCMB
        zhel = self.zHEL
        theory_ynew = 5.0*np.log10((1.0+zcmb)*(1.0+zhel)*np.atleast_1d(f(zcmb)))+25.
                
        # Add the absolute supernova magnitude and return
        M = block[names.supernova_params, "M"]
        return theory_ynew + M


# This takes our class and turns it into 
setup, execute, cleanup = PantheonLikelihood.build_module()
