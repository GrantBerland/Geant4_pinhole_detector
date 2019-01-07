
import pandas as pd
import numpy as np

from scipy.stats import norm, skewnorm


def calculateAnglePerParticle(fileName, hit_fileName, gap_in_cm, theta_actual, phi_actual, numParticles):
    # Read in raw hit data
    detector_hits = pd.read_csv('./data/' + str(hit_fileName) + '.csv',
                               names=["x", "z", "energy"],
                               dtype={"x":np.float64,"z":np.float64,"energy":np.float64},
                               sep=',',
                               engine='c')


    if len(detector_hits['x']) is 0:
        raise ValueError('No particle hits on detector!')


    def skewNormStatistics(dataSeries):
        # Returns skewnorm mean, stddev (see wikipedia for formulas)
        # alpha ~ shape parameter
        # loc   ~ location parameter
        # w     ~ scale parameter
        alpha, loc, w = skewnorm.fit(dataSeries)
        delta = alpha / np.sqrt(1 + alpha**2)
        skewnorm_mean = loc + w*delta*np.sqrt(2/np.pi)
        skewnorm_var  = (w**2)*(1 - 2*(delta**2)/np.pi)
        if skewnorm_var >= 0:
            skewnorm_std = np.sqrt(skewnorm_var)
        else:
            skewnorm_std = 999

        return (skewnorm_mean, skewnorm_std)


    # Find angles in degrees for centered pinhole in X, Z plane
    theta = np.rad2deg(np.arctan2(detector_hits["z"], gap_in_cm))
    phi = np.rad2deg(np.arctan2(detector_hits["x"], gap_in_cm))

    # Fit a standard normal distribution to data
    mu_theta, std_theta = norm.fit(theta)
    mu_phi, std_phi = norm.fit(phi)

    # Fit a skew normal distribution to data
    mu_theta_SN, std_theta_SN = skewNormStatistics(theta)
    mu_phi_SN, std_phi_SN = skewNormStatistics(phi)


    with open(fileName, 'a') as f:
        f.write(str(numParticles) +
        ',' + str(theta_actual) + ',' + str(phi_actual) +
        ',' + str(round(np.mean(theta), 4)) + ',' + str(round(np.std(theta), 4)) +
        ',' + str(round(np.mean(phi), 4)) + ',' + str(round(np.std(phi), 4)) +
        ',' + str(round(np.median(theta), 4)) + ',' + str(round(np.median(phi), 4)) +
        ',' + str(round(mu_theta, 4)) + ',' + str(round(std_theta, 4)) +
        ',' + str(round(mu_phi, 4)) + ',' + str(round(std_phi, 4)) +
        ',' + str(round(mu_theta_SN, 4)) + ',' + str(round(std_theta_SN, 4)) +
        ',' + str(round(mu_phi_SN, 4)) + ',' + str(round(std_phi_SN, 4)) + '\n')
