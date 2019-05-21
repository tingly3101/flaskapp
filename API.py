from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin

from Numerical import *

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)



@app.route('/' , methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def first_function():

    return """<h1>Hello world</h1>
    <h2>Hello world</h2>"""

# @app.route('/testFunction', methods=['GET','POST'])
# @cross_origin(support_credentials=True)
# def testFunction():
#     if(request.method == 'GET'):
#         return 'Get Method...'
#     elif(request.method == 'POST'):
#         return 'Post Method from ' + request.json['Input']
#     else:
#         abort(400)

@app.route('/trapezoidal', methods=['POST'])
@cross_origin(support_credentials=True)
def trapezoidalAPI():
    result = trapezoidal(int(request.json['a']),int(request.json['b']))
    return jsonify({'result':result})

@app.route('/composite_trapezoidal', methods=['POST'])
@cross_origin(support_credentials=True)
def composite_trapezoidalAPI():
    result = composite_trapezoidal(request.json['a'],request.json['b'],request.json['n'])
    return jsonify({'result':result})

@app.route('/bisection', methods=['POST'])
@cross_origin(support_credentials=True)
def bisectionAPI():
    result = bisection(request.json['xl'],request.json['xr'])
    return jsonify({'result':result})
#------------------------Numerical Function------------------
#แก้ไชฟังก์ชันที่จะนำไปคำนวนในนี้
def bi_func(x):
    # for Bisection method find value of sqrt(45)
    return x - pow(45, 0.5)
#function for trapzoidal to find area under graph
def func(x):
    #x^2+x+1
    return x*x+x+1

def bisection(xl,xr):
    result=[]
    n=0
    # err=100
    # print('fxl:',bi_func(xl),'fxr',bi_func(xr))
    if(not (xl<xr) and not((bi_func(xl)<0 and bi_func(xr)>0) or (bi_func(xl)>0 and bi_func(xr)<0)) ):
        print('Invalid function...')
        return
    while(n<1000):
        xm = float((xl + xr) / 2)
        result.append({'ite':n+1,'xl':xl,'xr':xr ,'xm':xm,'func(xm)':bi_func(xm)})
        # print('ite',n+1,'xl',xl,'xr',xr ,'xm',xm,'func(xm)',func(xm))
        if(bi_func(xl)*bi_func(xm)<0):
            # print('xr=xm')
            xr=xm
        elif(bi_func(xr)*bi_func(xm)<0):
            # print('xl=xm')
            xl=xm
        elif (bi_func(xm)==0):
            # print('found result')
            return result
        n=n+1

    return result

def trapezoidal(a,b):
    if(b>a):
        return float((b-a)/2)*(func(a)+func(b))
    else:
        return "Error Invalid parameter..."

def composite_trapezoidal(a,b,n):
    area=0
    if(b<a and int(b)<=1):
        return "Error Invalid parameter..."
    else:
        i=float(a)
        while(i < b):
            print(i,round(i + (b - a) / n,2))
            area = area +((b-a)/n)*(func(i)+func(round(i + (b - a) / n,2)))

            i= round(i + (b - a) / n,2)
    return area
#ทดสอบการยิง Rest API ด้วย method Get Post เพื่อทดสอบการตอบสนอง
if __name__ == '__main__':
    app.run(debug=False,host=(''))
