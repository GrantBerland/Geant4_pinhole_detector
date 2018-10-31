import pandas as pd
import numpy as np

class BaseImport:
    def __init__(self):

        # Instance variable
        data = import_hit_data()

    def import_hit_data(self):
        detector_hits = pd.read_csv('./data/hits.csv',
                                     names=["det","x", "y", "z","energy"],
                                     dtype={"det": np.int32, "x":np.float64,
                                            "y": np.float64, "z":np.float64},
                                     error_bad_lines=False,
                                     skiprows=1,
                                     engine='c')

        if len(detector_hits['det']) == 0:
            raise ValueError('No particles hits on either detector!')
        elif 2 not in detector_hits['det']:
            raise ValueError('No particles hit detector 2!')

        return detector_hits

 class BaseAnalysis(BaseImport):
     def __init__(self, window_to_det1_gap_in_cm: float):

         self._data = import_hit_data()
         self._gap = window_to_det1_gap_in_cm

     def calculateAnglePerParticle() -> List:
         deltaX = np.zeros(len(det), dtype=np.float64)
         deltaZ = np.zeros(len(det), dtype=np.float64)

         array_counter = 0
         for count, el in enumerate(det):
             # pandas series can throw a KeyError if character starts line
             while True:
                 try:
                     pos1 = det[count]
                     pos2 = det[count+1]

                     X[count]
                     Z[count]

                     X[count+1]
                     Z[count+1]
                 except:
                     count = count + 1
                     if count == len(det):
                         break
                     continue
                 break

             # Checks if first hit detector == 1 and second hit detector == 2
             if np.equal(pos1, 1) & np.equal(pos2, 2):
                 deltaX[array_counter] = X[count+1] - X[count]
                 deltaZ[array_counter] = Z[count+1] - Z[count]

                 # Successful pair, continues to next possible pair
                 count = count + 2
                 array_counter = array_counter + 1
             else:
                 # Unsuccessful pair, continues
                 count = count + 1

         # Remove trailing zeros
         deltaX_rm = deltaX[:array_counter]
         deltaZ_rm = deltaZ[:array_counter]

         del deltaX
         del deltaZ

         # Find angles in degrees
         theta = np.arctan2(deltaZ_rm, self._gap) * 180 / np.pi
         phi = np.arctan2(deltaX_rm, self._gap) * 180 / np.pi

         return [theta, phi]
