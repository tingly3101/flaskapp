from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)

@app.route('/')
@cross_origin(supports_credentials=True)
def first_function():
    return "Hello from flask"

