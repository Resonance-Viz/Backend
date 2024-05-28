from flask import Flask
from flask_cors import CORS

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.json_util import dumps

import os 

mongo_uri = os.environ.get('MONGO_URI')

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello from EC2 instance!'

@app.route('/formatted-data')
def get_data():
    return 'hi'
    # # Create a new client and connect to the server
    # client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)
    
    # collection = client['mock_ww_data']['character_usage']

    # return dumps(collection.find())
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  