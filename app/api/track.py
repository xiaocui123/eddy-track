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

def trackeddy(filepath='../input/nrt_global_allsat_phy_l4_20200815_20200815.nc',areadic=None):
    # Open netcdf Dataset.
    ncfile = Dataset(filepath)
    # Load data into memory
    sla = ncfile.variables['sla'][:]
    lon = ncfile.variables['longitude'][:]
    lat = ncfile.variables['latitude'][:]
    timeAttrStart = ncfile.getncattr("time_coverage_start")
    timeAttrEnd = ncfile.getncattr("time_coverage_end")

    # Define area of study
    # areamap = array([[0,len(lon)],[0,len(lat)]]) # Global option
    areamap = array([[1136,1248],[368,528]]) # Global option

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

    return positive_eddies