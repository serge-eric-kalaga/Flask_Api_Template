from flask_restx import fields

from flask import jsonify

from typing import Any, Dict


def response(status:int=1, data:Any="", status_code=200) -> Dict :
    var = {'status':status,'status_code': status_code, 'data': data }
    return var


def baseModel(name: str, namespace: object, dataModel: fields.Raw) -> Dict:
    resp = namespace.model(name, dataModel)
    return resp


def responseModel(name: str, namespace: object, dataModel: fields.Raw) -> Dict:
    resp = namespace.model(name, {
        'status': fields.Integer(),
        'status_code': fields.Integer(),
        'data': fields.Nested(dataModel)
    })
    return resp


def responseListModel(name: str, namespace: object, dataModel: fields.Raw) -> Dict:
    resp = namespace.model(name, {
        'status': fields.Integer(),
        'status_code': fields.Integer(),
        'data': fields.List(fields.Nested(dataModel))
    })
    return resp





