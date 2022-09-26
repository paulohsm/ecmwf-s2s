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

print(fp)

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
        d = xr.open_dataset(fp, autoclose=True)
        pr = d['pr']
        p = pr.sel(longitude=slice(-50, -30), latitude=slice(-20, 10))
        l = [hind, yy1, mm1, dd1, yy2, mm2, dd2, id0, p]
        prec.append(l)

# Test of read netcdf file
from netCDF4 import Dataset
from scipy.io import netcdf 
nc_file1 = '/run/media/santiago/ext2tb/dados/s2s-data/hind/ECMWF/1997/01/pr_daily_s2s_ecmwf_hind9716_20170102_19970102.nc'
nc_file2 = '/run/media/santiago/ext2tb/dados/s2s-data/hind/ECMWF/1997/01/pr_daily_s2s_ecmwf_hind9716_20170105_19970105.nc'
nc_data = Dataset(nc_file2)
nc_vars = nc_data.variables.keys()
print(nc_vars)
tmmm = nc_data['time']
print(tmmm[:])
prrr = nc_data['pr']
print(prrr[:, 0, 100, 100])
#nc_data = netcdf.NetCDFFile(nc_file, 'r')
#nc_vars = nc_data.variables[]