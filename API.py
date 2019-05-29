from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin



app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)



@app.route('/' , methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def first_function():

    return """<h1>Hello world</h1>
    <h2>Hello world</h2>"""


#ทดสอบการยิง Rest API ด้วย method Get Post เพื่อทดสอบการตอบสนอง
if __name__ == '__main__':
    app.run(debug=False,host=(''))
