
import re
import os
import requests

import urllib
import netCDF4
url='http://mrms.ncep.noaa.gov/data/2D/MESH_Max_60min/MRMS_MESH_Max_60min.latest.grib2.gz'
urllib.urlretrieve(url,'mesh.grib2.gz')
os.system(u'gunzip -f mesh.grib2.gz')
os.system(u'wgrib2 mesh.grib2 -small_grib -98:-87 37:47 mesh.region') #w,e,s,n
os.system(u'wgrib2 mesh.region -netcdf mesh.nc')
nc=netCDF4.Dataset('mesh.nc')
lat=nc.variables['latitude'][:]
lon=nc.variables['longitude'][:]
rot=nc.variables['MESHMax60min_500mabovemeansealevel'][:]

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shapely.geometry as sgeom
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import os
from time import gmtime, localtime, strftime
#title:
tt=strftime('%m/%d/%Y %I:%M %p %Z', localtime()) #%x %X %p %Z
#file:
tf=strftime("%m%d%Y/%H%M", localtime())
#directory 
td=strftime("%m%d%Y", localtime())
#vtt=strftime('%x', gmtime())

state=cfeat.NaturalEarthFeature(category='cultural',
                                name='admin_1_states_provinces',
                                scale='110m', facecolor='none')
lake=cfeat.NaturalEarthFeature(category='physical',
                                name='lakes',
                                scale='110m', facecolor='none')

fig = plt.figure(figsize=(15,15)) 
ax=plt.axes(projection=ccrs.LambertConformal())
ax.set_extent([-97,-88,46.5,38],ccrs.Geodetic()) #w,e,n,s 
ax.add_feature(state)
ax.add_feature(lake)

ti=ax.set_title('%s'%tt,fontsize=15,y=1.002,color='w', fontweight='bold')
ti.set_bbox(dict(color='black',alpha=0.65))

#uncomment next 2 lines for contours instead of colormesh
#con=range(10,90,20)
#ax.contour(lon,lat,rot.squeeze(),con,transform=ccrs.PlateCarree())
ax.pcolormesh(lon,lat,rot.squeeze(),transform=ccrs.PlateCarree(),cmap='ocean_r')

#save figure.*change 'path' to wanted path*
plt.savefig('path/%s.png'%tf,bbox_inches='tight',dpi=150)
print 'SAVED'