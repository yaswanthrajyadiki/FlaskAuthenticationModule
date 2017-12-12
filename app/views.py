from flask_restful import Resource


class HelloWorld(Resource):

    def get(self):
        sample = {
            "message": "Hello, World."
        }
        return sample

