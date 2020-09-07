from app.api import bp
from flask import jsonify
from app.api.errors import bad_request
from flask import request

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
    if('lon' not in data):
        return bad_request('must include lon fields')

    return jsonify(data)

