#!/usr/bin/python3.5

import pandas as pd
import numpy as np
from astroML.stats import fit_bivariate_normal
from scipy.stats import skew

from fncs.fnc_getDetectorHitData import getDetectorHitData

def fit2DnormalDistribution(detector, fitFlag):

    X, Z = getDetectorHitData(detector)

    # Descriptive statistics
    skew_x_dim = skew(X)
    skew_z_dim = skew(Z)

    med = [np.median(X), np.median(Z)]


    if fitFlag == 1:
        # Bivariate normal fit
        (mu_nr, sigmaX_nr,
             sigmaZ_nr, alpha_nr) = fit_bivariate_normal(X, Z, robust=True)
    elif fitFlag == 0:

         sigmaX_nr = np.std(X)
         sigmaZ_nr = np.std(Z)

         alpha_nr = None
         mu_nr = [np.mean(X), np.mean(Z)]



    Gauss2D_dist = {'Mean': mu_nr, 'Median': med,
                    'Sigma X': sigmaX_nr,
                    'Sigma Z': sigmaZ_nr, 'Alpha': alpha_nr,
                    'Skew X': skew_x_dim, 'Skew Z': skew_z_dim}


    return Gauss2D_dist
