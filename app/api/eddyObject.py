import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class EddyObject(object):
    def __init__(self,centerlon,centerlat,shapelon,shapelat):
        self.centerlon = centerlon
        self.centerlat = centerlat
        self.shapelon =shapelon
        self.shapelat = shapelat

    def toJSON(self):
        return json.dumps(self, cls=NumpyEncoder)

