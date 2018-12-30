#!/usr/bin/python3.5


import pandas as pd
import numpy as np

from scipy.stats import norm, skewnorm

# Extracts and returns actual inital particle source angles
from fnc_findSourceAngle import findSourceAngle

def calculateAnglePerParticle(gap_in_cm):
    # Read in raw hit data
    detector_hits = pd.read_csv('./data/hits.csv',
                               names=["x", "y", "z","energy"],
                               dtype={"x":np.float64,
                               "y": np.float64, "z":np.float64, "energy":np.float64},
                               delimiter=',',
                               error_bad_lines=False,
                               engine='c')


    if len(detector_hits['x']) is 0:
        raise ValueError('No particles hits on detector!')


    # Find angles in degrees
    theta = np.rad2deg(np.arctan2(detector_hits["z"], gap_in_cm))
    phi = np.rad2deg(np.arctan2(detector_hits["x"], gap_in_cm))

    # Fit a standard normal distribution to data
    try:
        x_theta = np.linspace(min(theta), max(theta))
        mu_theta, std_theta = norm.fit(theta)
        p_theta = norm.pdf(x_theta, mu_theta, std_theta)

        x_phi = np.linspace(min(phi), max(phi))
        mu_phi, std_phi = norm.fit(phi)
        p_phi = norm.pdf(x_phi, mu_phi, std_phi)

    except:
        x_theta = None
        mu_theta, std_theta = None, None
        p_theta = None

        x_phi = None
        mu_phi, std_phi = None, None
        p_phi = None

    theta_actual, phi_actual, numberOfParticles = findSourceAngle()

    with open('./data/results.txt', 'a') as f:
        f.write(str(numberOfParticles) +
        ',' + str(theta_actual) + ',' + str(phi_actual) +
        ',' + str(round(np.mean(theta), 4)) + ',' + str(round(np.std(theta), 4)) +
        ',' + str(round(np.mean(phi), 4)) + ',' + str(round(np.std(phi), 4)) +
        ',' + str(round(np.median(theta), 4)) + ',' + str(round(np.median(phi), 4)) +
        ',' + str(round(mu_theta, 4)) + ',' + str(round(std_theta, 4)) +
        ',' + str(round(mu_phi, 4)) + ',' + str(round(std_phi, 4)) + '\n')
