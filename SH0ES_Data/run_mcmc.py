'''
A minimum working example to run MCMC for SH0ES data.
Y.S.Murakami 2021-2022 @ JHU
'''
import numpy as np
from MCMC_utils import *

##### config #####
# change the variables below for desired data files, output path, MCMC settings, etc.

# least square fit results (for initial guess and constructing priors)
lstsq_results_path = 'data/lstsq_results.txt'

# file names for equation matrices
Y_fits_path = 'ally_shoes_ceph_topantheonwt6.0_112221.fits'
L_fits_path = 'alll_shoes_ceph_topantheonwt6.0_112221.fits'
C_fits_path = 'allc_shoes_ceph_topantheonwt6.0_112221.fits'

# default output file name
OUTPATH = "final_v2_baseline.h5"

# MCMC sampler settings
N_WALKERS = 100  # number of walkers
N_CHAIN  = 100   # length of chain for each walker
CONTD = False    # set CONTD = True to resume sampling (for specific OUTPATH)
# note: keeping CONTD = False may overwrite an existing file.

# Ratio between least-square fit STD to the half-width of uniform prior:
# this needs to be much larger than the width of posterior distribution
# but making it too large will cost more computing time.
# We found PRIOR_WIDTH_RATIO = 10 to be optimal
PRIOR_WIDTH_RATIO = 10

##### end of config #####


        
if __name__ == '__main__':
    # load least-square, bets-fit results by default
    #
    # note:
    # Passing manually defined arrays to 'lstsq_results' argument
    # and setting PRIOR_WIDTH_RATIO = 0 will allow users to define
    # the desired central values and width of the prior manually.
    # If you wish to use different (e.g., Gaussian) priors, define
    # the analytic Gaussian function in MCMC_utils.py file accordingly.
    q_lstsq, sigma_lstsq = np.loadtxt(lstsq_results_path,unpack=True)

    # run MCMC
    run_MCMC(nwalkers = N_WALKERS,
             chain = N_CHAIN,
             data_paths = [Y_fits_path, L_fits_path, C_fits_path],
             lstsq_results = [q_lstsq, sigma_lstsq],
             prior_width_ratio = PRIOR_WIDTH_RATIO,
             outpath = OUTPATH,
             contd = CONTD)
