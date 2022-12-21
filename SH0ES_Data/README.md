# DataRelease

## SH0ES-2022

May 19, 2022:
We are providing here "high level data products" for the full SH0ES+Panthon+ ladder.  The data is provided in the compact matrix form (linear equations) given in the paper, Riess et al. 2022, section 2.1 and equation 6, y=data vector, L=equation matrix (also includes some data), C=covariance matrix.  These are given as fits files.  Python code is provided to load these and to run an MCMC.  Results from these data files and code is shown in Figure 14 of Riess et al. (2022).  lstsq_results.txt constructs a 'prior' that is large enough to make it essentially prior-free. Please contact (ariess@stsci.edu) if you see a problem.

allc_shoes_ceph_topantheonwt6.0_112221.fits=C, covariance matrix

alll_shoes_ceph_topantheonwt6.0_112221.fits=L, equation matrix

ally_shoes_ceph_topantheonwt6.0_112221.fits=y, data vector

NOTE: an initial slope term of -3.285 was used for the calculation so that the free parameter slope (which will appear as a small ~0 number) must be added back to -3.285 to recover the true slope term 



Jan-2022: We are first making publicly available the new measurements of Cepheids in the optical and NIR as described in Riess et al. 2022 and Yuan et al. 2022
for the hosts of the original 19 SN Ia in Riess et al. (2016), NGC 4258 and the LMC which will allow one to do the style of analysis such as in Riess et al. (2016) with the pre-new release sample.  The expanded sample data and covariance matrix needed to use it will become available in the near term.  Please see details in those two papers which describe the new data and the various calibrations and improvements made over what was previously available.  As this is a new data release with real improvements, please use this instead of a prior data product.

https://arxiv.org/pdf/2112.04510.pdf

https://arxiv.org/pdf/2203.06681.pdf

-The new optical-only Cepheid data from SH0ES in the Riess et al (2022) and Yuan et al. (2022) for the original 19 hosts from R16 as well as the new NGC 4258 and LMC data - `optical_wes_R22_for19fromR16.dat`   Note that the optical Wesenheit errors are over-estimated by ~15% due to the cotrrelation between V and I background errors.

The new NIR Cepheid data from SH0ES in the Riess et al (2022) and Yuan et al. (2022) for the original 19 hosts from R16 as well as the new NGC 4258 and LMC data - `R22_orig19_NIR.out`


Dec 12, 2022:
Table 2 has been uploaded (and associated readme)
