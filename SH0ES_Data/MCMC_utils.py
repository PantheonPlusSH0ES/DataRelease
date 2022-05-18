'''
A simple code to run MCMC for SH0ES results.
Y.S.Murakami September 2021 @ JHU
'''
import numpy as np
from scipy import linalg
from astropy.io import fits
try:
    import emcee
except Exception:
    print('emcee is required to run this code. Try \'pip install emcee\'.')

def log_prior(theta,priors):
    '''
    log-prior for the parameters (uniform)
    '''
    mu,halfwidth = priors
    for i in range(len(theta)):
        if theta[i]>mu[i]+halfwidth[i] or theta[i]<mu[i]-halfwidth[i]:
            return -np.inf
    return 1

def log_probability(theta,Y,L,C,C_inv_cho,priors):
    '''
    log-probability that governs the rate of acceptance for given proposed parameter.
    '''
    lp = log_prior(theta,priors)
    if not np.isfinite(lp):
        return -np.inf
    ll = log_likelihood(theta,Y,L,C,C_inv_cho)
    if not np.isfinite(ll):
        return -np.inf
    return lp + ll

def log_likelihood(theta,Y,L,C,C_inv_cho):
    res = Y-np.dot(theta,L)
    chi2 = np.dot(res,np.dot(C_inv_cho,res))
    return -0.5*chi2 # normalization is constant so can be omitted

def run_MCMC(nwalkers,chain,data_paths,lstsq_results,
             prior_width_ratio,outpath=None,contd=False):
    '''
    a wrapper file
    '''
    if outpath is None:
        outpath = './results.h5'
    # load data
    Y_fits_path, L_fits_path, C_fits_path = data_paths
    Y = fits.open(Y_fits_path)[0].data
    L = fits.open(L_fits_path)[0].data
    C = fits.open(C_fits_path)[0].data
    
    # prepare inverse of C-matrix
    C_inv_cho = linalg.cho_solve(linalg.cho_factor(C),np.identity(C.shape[0]))

    # priors
    q_lstsq, sigma_lstsq = lstsq_results
    mu_list = q_lstsq
    width_list = sigma_lstsq * prior_width_ratio
    priors = [mu_list,width_list]
    
    # initial guess array for each walker: 
    x0 = np.random.uniform(mu_list-width_list,
                           mu_list+width_list,
                           size=(nwalkers,len(mu_list)))
    nwalkers, ndim = x0.shape
    
    # save file
    backend = emcee.backends.HDFBackend(outpath)
    if contd:
        print(f'initial size: {backend.iteration}',flush=True)
    else:
        backend.reset(nwalkers, ndim)
    
    # initialize sampler, run MCMC
    sampler = emcee.EnsembleSampler(nwalkers, 
                                    ndim, 
                                    log_probability,
                                    args = [Y,L,C,C_inv_cho,priors],
                                    backend = backend)
    
    if contd:
        sampler.run_mcmc(None, chain, progress=True,skip_initial_state_check=True);
        print(f'final size: {backend.iteration}',flush=True)
    else:
        sampler.run_mcmc(x0, chain, progress=True,skip_initial_state_check=True);