import os
os.environ['PROJ_LIB'] = "/opt/tljh/user/share/proj"

# Importing all libraries.
from pylab import *
from netCDF4 import Dataset
import os
import cmocean as cm
from trackeddy.tracking import *
from trackeddy.datastruct import *
from trackeddy.geometryfunc import *
#from trackeddy.init import *
from trackeddy.physics import *
from trackeddy.plotfunc import *

import matplotlib.pyplot as plt
from app.api.eddyObject import EddyObject
from app.api.eddyObject import NumpyEncoder
import json

def trackeddy(filepath='../input/nrt_global_allsat_phy_l4_20200815_20200815.nc',lon0=None,lon1=None,lat0=None,lat1=None):
    # Open netcdf Dataset.
    ncfile = Dataset(filepath)
    # Load data into memory
    sla = ncfile.variables['sla'][:]
    lon = ncfile.variables['longitude'][:]
    lat = ncfile.variables['latitude'][:]
    timeAttrStart = ncfile.getncattr("time_coverage_start")
    timeAttrEnd = ncfile.getncattr("time_coverage_end")

    # Define area of study
    if lon0 is not None:
        areamap = array([[0,len(lon)],[0,len(lat)]]) # Global option
    else:
        areamap = array([[lon0,lon1],[lat0,lat1]]) # Global option

    print(areamap)
    print("scope {0} {1} {2} {3}".format(lat[lat0],lat[lat1],lon[lon0],lon[lon1]))
    # Time and spatial filter
    filters = {'time': {'type': None, 't': None, 't0': None, 'value': None},
               'spatial': {'type': 'moving', 'window': 50, 'mode': 'uniform'}}

    # Mesoscale scaling
    checkarea = {'mesoscale': 2 * np.pi}

    # Eddy definition criteria
    preferences = {'ellipse': 0.85, 'eccentricity': 0.85, 'gaussian': 0.8}

    # Levels to be analysed and to extract positive eddies from anomaly
    levels = {'max': sla[0, :, :].max(), 'min': 0.01, 'step': 0.03}

    positive_eddies = analyseddyzt(sla, lon, lat, 0, 1, 1, levels, preferences=preferences
                                   , areamap=areamap, areaparms=checkarea, filters=filters
                                   , maskopt='contour', diagnostics=False, pprint=True)

    eddyies = []
    for key in positive_eddies.keys():
        value = positive_eddies.get(key)
        centerlon = value["position_default"][0][0]
        centerlat = value["position_default"][0][1]

        ellipse = value["ellipse"]
        shapelon = json.dumps(ellipse[0][0],cls = NumpyEncoder)
        shapelat = json.dumps(ellipse[0][1],cls = NumpyEncoder)
        eddyies.append(EddyObject(timeAttrStart,centerlon,centerlat,shapelon,shapelat).toJSON())

    return eddyies
