from flask_restx import fields
from flask import jsonify
from typing import Any



def response(status:int=1, data:Any="", status_code=200) -> dict :
    var = {'status':status,'status_code': status_code, 'data': data }
    return var



def responseModel(name: str, namespace: object, dataModel: fields.Raw):
    resp = namespace.model(name, {
        'status': fields.Integer(),
        'data': fields.Nested(dataModel)
    })
    return resp



def responseListModel(name: str, namespace: object, dataModel: fields.Raw):
    resp = namespace.model(name, {
        'status': fields.Integer(),
        'data': fields.List(fields.Nested(dataModel))
    })
    return resp


# def responseModel(namespace, model:dict):
#     model = namespace.model(
#         name="TaskResponseModel",
#         model=response(data=model)
#     )  
#     return model


# def responseListModel(namespace, model:dict):
#     model = namespace.model(
#         name="TaskResponseModel",
#         model=response(data=fields.List(fields.Nested(model)))
#     )  
#     return model
