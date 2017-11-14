"""
Antenna-Microwave Noise Temperature Parameters, Referenced to Feedhorn

The table below is takeng fro 810-005 module 101, Table A3.

Unless crab14 is fixed, python command line tests should do this before imports
import IPython
IPython.version_info = IPython.release.version.split('.')
IPython.version_info.append('')
"""
from numpy import array

# note that each row below must be a tuple, not a list
noise_pars = array([
 ("L", 0,  "",         "LNA 1/2", "HEMT",  "non-diplexed",              26.67, 15.66, 0.09),
 ("S", 14, "SPD cone", "LNA-1",   "HEMT",  "non-diplexed",              12.17,  4.49, 0.05),
 ("S", 14, "SPD cone", "LNA-1",   "HEMT",  "diplexed",                  15.81,  4.55, 0.05),
 ("S", 14, "Mod III",  "LNA-2",   "HEMT",  "non-diplexed",              18.74,  4.61, 0.05),
 ("S", 14, "Mod III",  "LNA-2",   "HEMT",  "diplexed",                  23.69,  4.67, 0.05),
 ("S", 43, "SPD cone", "LNA-1",   "HEMT",  "non-diplexed",              13.57, 21.95, 0.14),
 ("S", 43, "SPD cone", "LNA-1",   "HEMT",  "diplexed",                  17.67, 22.26, 0.14),
 ("S", 43, "Mod III",  "LNA-2",   "HEMT",  "non-diplexed",              19.59, 22.51, 0.14),
 ("S", 43, "Mod III",  "LNA-2",   "HEMT",  "diplexed",                  24.72, 22.83, 0.14),
 ("S", 63, "SPD cone", "LNA-1",   "HEMT",  "non-diplexed",              15.27,  4.70, 0.057),
 ("S", 63, "SPD cone", "LNA-1",   "HEMT",  "diplexed",                  18.98,  4.76, 0.057),
 ("S", 63, "Mod III",  "LNA-2",   "HEMT",  "non-diplexed",              21.20,  4.82, 0.057),
 ("S", 63, "Mod III",  "LNA-2",   "HEMT",  "diplexed",                  26.82,  4.88, 0.057),
 ("X", 14, "",         "LNA-1",   "HEMT",  "RCP, X-only configuration", 11.63, 7.11, 0.065),
 ("X", 14, "",         "LNA-2",   "HEMT",  "LCP, X-only configuration", 11.63, 7.11, 0.065),
 ("X", 14, "",         "LNA-1",   "HEMT",  "RCP, S/X configuration",    12.57, 7.11, 0.065),
 ("X", 14, "",         "LNA-2",   "HEMT",  "LCP, S/X configuration",    12.57, 7.11, 0.065),
 ("X", 43, "",         "LNA-1",   "HEMT",  "RCP, X-only configuration", 12.09, 6.76, 0.070),
 ("X", 43, "",         "LNA-2",   "HEMT",  "LCP, X-only configuration", 12.09, 6.76, 0.070),
 ("X", 43, "",         "LNA-1",   "HEMT",  "RCP, S/X configuration",    13.32, 10.49, 0.100),
 ("X", 43, "",         "LNA-2",   "HEMT",  "LCP, S/X configuration",    13.32, 10.49, 0.100),
 ("X", 63, "",         "LNA-1",   "HEMT",  "RCP, X-only configuration", 11.45, 8.07, 0.077),
 ("X", 63, "",         "LNA-2",   "HEMT",  "LCP, X-only configuration", 11.45, 8.07, 0.077),
 ("X", 63, "",         "LNA-1",   "HEMT",  "RCP, S/X configuration",    12.62, 4.84, 0.060),
 ("X", 63, "",         "LNA-2",   "HEMT",  "LCP, S/X configuration",    12.62, 4.84, 0.060)],
dtype={"names":  ['band', 'DSS', 'location', 'LNA', 'type', 'config', 'T1',  'T2',  'a'],
       "formats":['a1',   'i4',  'a8',       'a8',  'a8',   'a32',    'f8',  'f8',  'f8']})

T1 = {14: {'L': {},
           'S': {},
           'X': {'R': {'SX': 12.57,
                       'X':  11.63},
                 'L': {'SX': 12.57,
                       'X':  11.63}}},
      43: {'L': {},
           'S': {},
           'X': {'R': {'SX': 13.32,
                       'X':  11.45},
                 'L': {'SX': 13.32,
                       'X' : 12.09}}},
      63: {'L': {},
           'S': {},
           'X': {'R': {'SX': 12.62,
                       'X':  11.45},
                 'L': {'SX': 12.62,
                       'X' : 11.45}}}}
T2 = {14: {'L': {},
           'S': {},
           'X': {'R': {'SX': 7.11,
                       'X':  7.11},
                 'L': {'SX': 7.11,
                       'X':  7.11}}},
      43: {'L': {},
           'S': {},
           'X': {'R': {'SX': 10.49,
                       'X':  6.72},
                 'L': {'SX': 10.49,
                       'X' : 6.72}}},
      63: {'L': {},
           'S': {},
           'X': {'R': {'SX': 4.84,
                       'X':  8.07},
                 'L': {'SX': 4.84,
                       'X' : 8.07}}}}
a  = {14: {'L': {},
           'S': {},
           'X': {'R': {'SX': 0.065,
                       'X':  0.065},
                 'L': {'SX': 0.065,
                       'X':  0.065}}},
      43: {'L': {},
           'S': {},
           'X': {'R': {'SX': 0.1,
                       'X':  0.07},
                 'L': {'SX': 0.1,
                       'X' : 0.07}}},
      63: {'L': {},
           'S': {},
           'X': {'R': {'SX': 0.06,
                       'X':  0.077},
                 'L': {'SX': 0.06,
                       'X' : 0.077}}}}

