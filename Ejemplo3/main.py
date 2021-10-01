from flask import Flask,request,abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def getuser():
    if request.method == 'GET':
        return ""
    if request.method == 'POST':
        return ""
    if request.method == 'DELETE':
        return ""
    else:
        abort(405)

app.run(host='0.0.0.0', port=81)
