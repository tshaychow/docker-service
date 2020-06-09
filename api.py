from flask import Flask
from flask_restful import Resource, Api
import numpy as np
import json

app = Flask(__name__)
api = Api(app)

class Content(Resource):
    def get(self): 
        return{
            'output': json.dumps((np.random.normal(0,1,10000)).tolist())
        }


api.add_resource(Content,'/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80, debug=True)
