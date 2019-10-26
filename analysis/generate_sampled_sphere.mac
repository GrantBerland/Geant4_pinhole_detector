import random as rand
import numpy as np

rand.seed()	# starts the Mersenne Twister rand engine

num_sources = 100
sphereR = 30  # cm

counter = 1

with open('rand_sphere.mac', 'w') as f:
    # init lines to set up simulation
    f.write('/run/initialize \n')
    f.write('/control/verbose 0 \n')
    f.write('/run/verbose 0 \n')
    f.write('/event/verbose 0 \n')
    f.write('/tracking/verbose 0 \n')

    for i in range(0, num_sources):

        theta_rand = rand.uniform(0, 2*np.pi)
        phi_rand   = rand.uniform(0, np.pi)

        # Positions on sphere of radius R
        x_pos = sphereR * np.sin(theta_rand) * np.cos(phi_rand)
        y_pos = sphereR * np.sin(theta_rand) * np.sin(phi_rand)
        z_pos = sphereR * np.cos(phi_rand)

        position_string = str(x_pos) + ' ' + str(y_pos) + ' ' + str(z_pos) + ' cm'

        # Draw random particle directions
        x_dir = rand.uniform(0, 1)
        y_dir = rand.uniform(0, 1)
        z_dir = rand.uniform(0, 1)

        # Enforce inward particle direction
        if x_pos > 0:
            x_dir = -x_dir
        if y_pos > 0:
            y_dir = -y_dir
        if z_pos > 0:
            z_dir = -z_dir

        direction_string = str(x_dir) + ' ' + str(y_dir) + ' ' + str(z_dir)

        f.write('\n# Particle source ' + str(counter) + '\n')
        f.write('/gps/source/add ' + str(i+1) + '\n')
        f.write('/gps/particle e-\n')
        f.write('/gps/ene/min 100. keV \n')
        f.write('/gps/ene/max 10. MeV \n')
        f.write('/gps/position ' + position_string + '\n')
        f.write('/gps/direction ' + direction_string + '\n')
        f.write('/gps/pos/type Point \n')

        counter = counter + 1

    f.write('\n/run/beamOn ' + str(num_sources) + '\n')

    f.close()
