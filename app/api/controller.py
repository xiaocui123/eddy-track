from app.api import bp
from flask import jsonify
from app.api.errors import bad_request
from flask import request
from app.api.track import track

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
    eddie = track(data['filepath'])
    return jsonify(eddie)

