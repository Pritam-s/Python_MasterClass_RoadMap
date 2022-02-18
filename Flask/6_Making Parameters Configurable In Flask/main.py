from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json


with open('Flask\\6_Making Parameters Configurable In Flask\config.json') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_test'
db = SQLAlchemy(app)



class Contacts(db.Model):
    class Contacts(db.Model):
        sno = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        phone_num = db.Column(db.String(12), nullable=False)
        msg = db.Column(db.String(120), nullable=True)
        email = db.Column(db.String(20), nullable=False)
    

@app.route('/')
def home():
    return render_template('index.html', params=params)

@app.route('/about')
def about():
    return render_template('about.html', params=params)

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg =message,email = email )
        db.session.add(entry)
        db.session.commit()
    
    return render_template('contact.html', params=params)



@app.route('/services.html')
def services():
    return render_template('services.html', params=params)

app.run(debug=True)