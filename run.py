from app import start_app
from flask import request
# from app.database import db

app = start_app()


# @app.route("/test/<string:tenant>")
# def test(tenant):
#     return tenant



# @app.before_request
# def before_request():
#     db.choose_tenant(request.args['tenant'])
#     db.create_all()


if __name__ == "__main__" :
    app.run(debug=True)
