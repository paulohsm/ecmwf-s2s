#from netCDF4 import Dataset

#s2s_file = '/run/media/santiago/ntfs-data/s2s/hind/ECMWF/1997/01/pr_daily_s2s_ecmwf_hind9716_20170102_19970102_10.nc'
#s2s_data = Dataset(s2s_file)

#interrogatin dimensions
#print s2s_data.dimensions.keys()

#interrogating variables
#print s2s_data.variables.keys()

#print s2s_data.variables['pr']
#pr = s2s_data.variables['pr']

#variable attributes
#print pr.units

#print s2s_data['time'][:]

#print pr[:][:][0] + pr[:][:][1] + pr[:][:][2] + pr[:][:][3] + pr[:][:][4]
#print sum(pr[:][:][0:6])
#print s2s_data['time'][:]
#print sum(pr[:][:][7:13])


################################
## generate a list of file paths
from glob import glob
bdir = '/run/media/santiago/ntfs-data/s2s/hind/ECMWF'
flist = []
for yy in range(1997, 2018):
    for mm in range(1, 13):
        mmfl = sorted(glob(bdir + '/' + str(yy) + '/' + str(mm) + '/' + '*.nc'))
        for fp in mmfl:
            flist.append(fp)

# tutorial xarray
# https://gitlab.com/marcelorodriguesss/python_faq_coding/blob/master/xarray.ipynb

############
## load data
## neb = 50W, 30W, 20S, 5N
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
        #print(hind, yy1, mm1, dd1, yy2, mm2, dd2, id0, p)
        print(l)
        prec.append(l)

print(len(flist[0]))

## plot some sample
print(prec[10][8])
#import matplotlib.pyplot as plt
#prec[10][8].plot()
#plt.show()


#from netCDF4 import Dataset
#from scipy import interpolate
#lons = s2s_data.variables['longitude']
#lats = s2s_data.variables['latitude']
#for fp in flist:
#    hind = os.path.basename(fp)[23:27]
#    yy1 = os.path.basename(fp)[28:32]
#    mm1 = os.path.basename(fp)[32:34]
#    dd1 = os.path.basename(fp)[34:36]
#    yy2 = os.path.basename(fp)[37:41]
#    mm2 = os.path.basename(fp)[41:43]
#    dd2 = os.path.basename(fp)[43:45]
#    id0 = os.path.basename(fp)[46:48]
#    d = Dataset(fp)
#    pr = d.variables['pr']
