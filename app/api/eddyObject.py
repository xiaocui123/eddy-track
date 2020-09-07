import json
class EddyObject(object):
    def __init__(self,centerlon,centerlat,shapelon,shapelat):
        self.centerlon = centerlon
        self.centerlat = centerlat
        self.shapelon =shapelon
        self.shapelat = shapelat

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

