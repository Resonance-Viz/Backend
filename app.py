from flask import Flask
from flask_cors import CORS

import logging

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.json_util import dumps

import os 

logging.basicConfig(filename='app.log', level=logging.DEBUG)

mongo_uri = os.environ.get('MONGO_URI')

def create_app():
    app = Flask(__name__)

    with app.app_context():
        client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            logging.error(e)
            print(e)   
    
        @app.route('/')
        def hello_world():
            return 'Hello from EC2 instance!'

        @app.route('/formatted-data')
        def get_data():
            # # Create a new client and connect to the server
            # collection = client['mock_ww_data']['character_usage']

            # return dumps(collection.find())
            
            return str(mongo_uri)
     
    return app

if __name__ == '__main__':
    app = create_app()
    CORS(app)
    app.run(host='0.0.0.0', port=5000)  