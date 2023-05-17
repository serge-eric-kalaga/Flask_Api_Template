from flask_restx import fields
from flask import jsonify
from typing import Any


# def responseModel(name:str, namespace:object, dataModel:Any,):
#     resp = namespace.model(name ,{'status':fields.Integer(), 'data':fields.Nested(dataModel)})
#     return resp


# def responseListModel(name:str, namespace:object, dataModel:Any):
#     resp = namespace.model(name ,{'status':fields.Integer(), 'data':fields.List(fields.Nested(dataModel))})
#     return resp


def response(status:int=1, data:Any="", status_code=200):
    var = {'status':status,'status_code': status_code, 'data': data }
    return var