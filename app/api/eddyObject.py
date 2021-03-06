import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class EddyObject(object):
    def __init__(self,datetime,centerlon,centerlat,shapelon,shapelat):
        self.datetime = datetime
        self.centerlon = centerlon
        self.centerlat = centerlat
        self.shapelon =shapelon
        self.shapelat = shapelat

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

