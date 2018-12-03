from flask import Flask
from flask_restful import Resource, Api
from decode import decode

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class ArtifactCodeDeck(Resource):
    def get(selfs,deck_code):
        return {'deck':decode(deck_code)}


api.add_resource(HelloWorld, '/')
api.add_resource(ArtifactCodeDeck,'/CodeDeck/<string:deck_code>')

if __name__ == '__main__':
    app.run(debug=True)
