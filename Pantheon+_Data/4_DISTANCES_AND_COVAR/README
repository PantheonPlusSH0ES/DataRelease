Nominal SN and Cepheid-host Distances used in
  Pantheon+ arXiv:2202.04077
  SH0ES arXiv:2112.04510
are provided in Pantheon+SH0ES.dat

Statistical and Stat+Systematic Covariance matrices are provided in
Pantheon+SH0ES_STATONLY.cov
Pantheon+SH0ES_STAT+SYS.cov (all systematics)

Covariances for specific sources of systematics can be found in sytematic_groupings/

The format of the covariance (.cov) file is NxN lines where the matrix should be read in sequentially.  The first line gives the number of rows/columns in the matrix (N=1701).  The STATONLY matrix has only elements that correspond to the statistical distance uncertainties for individual SNe. This includes intrinsic scatter off-diagonal components when the light-curves represent the same SN observed by different surveys. The STAT+SYS matrix also includes all the covariance between SNe (and also Cepheid host covariance) due to systematic uncertainties.

Pantheon+SH0ES.dat Column Definitions: 
  CID - Candidate ID
  IDSURVEY - {1:'SDSS', 4:'SNLS', 5:'CSP', 10:'DES', 15:'PS1MD', 18:’CNIa0.02’, 50:'LOWZ/JRK07', 51:'LOSS1', 56:'SOUSA', 57:’LOSS2’, 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 100:'HST', 101:'SNAP', 106:'CANDELS', 150:'FOUND'}
  zHD - Hubble Diagram Redshift (with CMB and VPEC corrections)
  zHDERR - Hubble Diagram Redshift Uncertainty
  zCMB - CMB Corrected Redshift
  zCMBERR - CMB Corrected Redshift Uncertainty 
  zHEL - Heliocentric Redshift
  zHELERR - Heliocentric Redshift Uncertainty
  m_b_corr - Tripp1998 corrected/standardized m_b magnitude
  m_b_corr_err_DIAG - Tripp1998 corrected/standardized m_b magnitude uncertainty as determined from the diagonal of the covariance matrix. **WARNING, DO NOT FIT COSMOLOGICAL PARAMETERS WITH THESE UNCERTAINTIES. YOU MUST USE THE FULL COVARIANCE. THIS IS ONLY FOR PLOTTING/VISUAL PURPOSES**
  MU_SH0ES - Tripp1998 corrected/standardized distance modulus where fiducial SNIa magnitude (M) has been determined from SH0ES 2021 Cepheid host distances.
  MU_SH0ES_ERR_DIAG - Uncertainty on MU_SH0ES as determined from the diagonal of the covariance matrix. **WARNING, DO NOT FIT COSMOLOGICAL PARAMETERS WITH THESE UNCERTAINTIES. YOU MUST USE THE FULL COVARIANCE. THIS IS ONLY FOR PLOTTING/VISUAL PURPOSES**
  CEPH_DIST - cepheid calculated absolute distance to host (uncertainty is incorporated in covariance matrix .cov)
  IS_CALIBRATOR - binary to designate if this SN is in a host that has an associated cepheid distance
  USED_IN_SH0ES_HF - 1 if used in SH0ES 2021 Hubble Flow dataset. 0 if not included.
  c - SALT2 color
  cERR - SALT2 color uncertainty
  x1 - SALT2 stretch
  x1ERR - SALT2 stretch uncertainty
  mB - SALT2 uncorrected brightness
  mBERR - SALT2 uncorrected brightness uncertainty
  x0 - SALT2 light curve amplitude
  x0ERR - SALT2 light curve amplitude uncertainty
  COV_x1_c - SALT2 fit covariance between x1 and c
  COV_x1_x0 - SALT2 fit covariance between x1 and x0
  COV_c_x0 - - SALT2 fit covariance between c and x0
  RA - Right Ascension 
  DEC - Declination
  HOST_RA - Host Galaxy RA
  HOST_DEC - Host Galaxy DEC
  HOST_ANGSEP - Angular separation between SN and host (arcsec)
  VPEC - Peculiar velocity (km/s)
  VPECERR - Peculiar velocity uncertainty (km/s)
  MWEBV - Milky Way E(B-V)
  HOST_LOGMASS - Host Galaxy Log Stellar Mass
  HOST_LOGMASS_ERR - Host Galaxy Log Stellar Mass Uncertainty
  PKMJD - Fit Peak Date
  PKMJDERR  - Fit Peak Date Uncertainty
  NDOF - Number of degrees of freedom in SALT2 fit
  FITCHI2 - SALT2 fit chi squared
  FITPROB - SNANA Fitprob
  m_b_corr_err_RAW - statistical only error on the fitted m_B
  m_b_corr_err_VPEC - VPECERR propagated into a magnitude error assuming a fiducial LCDM cosmology
  biasCor_m_b - Bias correction applied to brightness m_b
  biasCorErr_m_b  - Uncertainty on bias correction applied to brightness m_b
  biasCor_m_b_COVSCALE - Reduction in uncertainty due to selection effects (multiplicative)
  biasCor_m_b_COVADD  - Uncertainty floor as given by the intrinsic scatter model (quadriture)

