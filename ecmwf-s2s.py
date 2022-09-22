# ECMWF Subseazonal to seasonal forecast analysis for brazilian northeast (neb) precipitation.

# Directory path where initial data is stored
bdir = '/run/media/santiago/ext2tb/dados/s2s-data/hind/ECMWF/'

# basic data information
y1 = 1997
y2 = 2018

# generate list of file paths
from glob import glob
flist = []
for yy in range(y1, y2):
    for mm in range(1, 13):
        mmfl = sorted(glob(bdir + '/' + str(yy) + '/' + str(mm) + '/' + '*.nc'))
        for fp in mmfl:
            flist.append(fp)

# load data / neb limits = 50W, 30W, 20S, 5N
import xarray as xr
import os 
prec = []
for fp in flist:
    if os.path.exists(fp):
        hind = os.path.basename(fp)[23:27]
        yy1 = os.path.basename(fp)[28:32]
        mm1 = os.path.basename(fp)[32:34]
        dd1 = os.path.basename(fp)[34:36]
        yy2 = os.path.basename(fp)[37:41]
        mm2 = os.path.basename(fp)[41:43]
        dd2 = os.path.basename(fp)[43:45]
        id0 = os.path.basename(fp)[46:48]
        