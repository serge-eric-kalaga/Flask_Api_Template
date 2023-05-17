from flask_restx import Resource, fields, Namespace


hello_namespace = Namespace("Hello", description="Test Hello")


@hello_namespace.route("/" )
class Hello(Resource):
    
    def get(self):
        return "Hello world"
    

