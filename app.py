from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin
from pythainlp import word_tokenize
import time

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)

@app.route('/')
@cross_origin(support_credentials=True)
def default():
    return 'hello default'

@app.route('/api/wordseg', methods=['GET','POST'])
@cross_origin(support_credentials=True)
def first_function():
    if request.method == 'POST':
        start = time.time()
        """text:str hybrid tokenize will be merge between newmm and deepcut to select longest-matching"""
        Input = request.json['text']
        newmm_res = word_tokenize(Input)
        deepcut_res = word_tokenize(Input, engine='deepcut')
        hybrid_tokenize = []
        i = 0
        j = 0
        word_L = []
        word_R = []
        while i < len(newmm_res) and len(deepcut_res):
            if newmm_res[i] == deepcut_res[j]:
                # ทั้ง2แบบเหมือนกัน
                hybrid_tokenize.append(newmm_res[i])
                i += 1
                j += 1
            else:
                word_L.append(newmm_res[i])
                word_R.append(deepcut_res[j])
                i += 1
                j += 1
                while (''.join(word_L) != ''.join(word_R)):
                    if (len(''.join(word_L)) < len(''.join(word_R))):
                        word_L.append(newmm_res[i])
                        i += 1
                    elif (len(''.join(word_L)) > len(''.join(word_R))):
                        word_R.append(deepcut_res[j])
                        j += 1
                hybrid_tokenize.append(''.join(word_L))
                word_L = []
                word_R = []
        result = {'newmm': '|'.join(newmm_res), 'deepcut': '|'.join(deepcut_res), 'hybrid': '|'.join(hybrid_tokenize),"time_res":'{} sec.'.format(time.time()-start)}
        return jsonify(result)
    else:
        return "method unavailable"

    
if __name__ == '__main__':
    app.run()


