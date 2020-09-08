from app.api import bp
from flask import jsonify
from app.api.errors import bad_request
from flask import request
from app.api.track import trackeddy

@bp.route('/rest/info',methods = ['GET'])
def info():
    data = {
        'name':'flask',
        'age':13
    }
    return jsonify(data)

@bp.route('/rest/track',methods = ['POST'])
def track():
    data = request.get_json() or {}
    if 'filepath' not in data:
        return bad_request('must include filepath fields')
    if data['lat0Index'] is not None:
        eddie = trackeddy(filepath=data['filepath'],lon0=data['lon0Index'],lon1=data['lon1Index'],lat0=data['lat0Index'],lat1=data['lat1Index'])
    else:
        eddie = trackeddy(filepath=data['filepath'])
    return jsonify(eddie)

