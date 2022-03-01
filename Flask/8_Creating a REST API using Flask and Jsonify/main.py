from flask import Flask, jsonify
import json
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({ 
        'name' : 'Nikku',
        'email' : 'Pritamsingh17@pm.me',
        'number': 8097150258,
        'items':['laptop', 98, True, 54.23]
    })

@app.route('/add/<int:a>,<int:b>')
def add(a,b):
    result = ({
        "First Number" : a,
        "Second Number" : b,
        f"Addition of {a} & {b} is" : a+b
        })
    return jsonify (result)



if __name__ == '__main__':
    app.run(debug= True)