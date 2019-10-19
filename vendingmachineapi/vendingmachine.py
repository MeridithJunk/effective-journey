from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Money(Resource):
    def get(self):
        return self.getcointamount(request.json['weight'])

    def getcointamount(self, weight):
        if weight == 5.00:
            return {'Money': 0.05}
        if weight == 2.268:
            return {'Money': 0.10}
        if weight == 5.670:
            return {'Money': 0.25}


api.add_resource(Money, '/money')

if __name__ == '__main__':
    app.run()
