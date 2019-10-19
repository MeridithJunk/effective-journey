from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Money(Resource):
    def get(self):
        print(request.json)
        weight = request.json['weight']
        return {'Money': 0.05}


api.add_resource(Money, '/money')


if __name__ == '__main__':
    app.run()
