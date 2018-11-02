#!/usr/bin/python3.5

def writeConfigFile(pinhole_rad_mm, window_gap_mm, window_t_mm):
    with open('../src/pinhole_config.txt','w') as f:
        f.write(str(pinhole_rad_mm) + '\n')
        f.write(str(window_gap_mm) + '\n')
        f.write(str(window_t_mm) + '\n')
