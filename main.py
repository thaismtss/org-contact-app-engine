from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
from service import get_credentials

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


class HelloWorld(Resource):
    def get(self):
        return make_response(render_template('gen/index.html'))


class Credentials(Resource):
    def post(self):
        credentials = request.json
        return get_credentials(credentials)


api.add_resource(HelloWorld, '/')
api.add_resource(Credentials, '/static/gen/contacts')
