#1. Taking help from documentation🧾 of flask, flask-alchemy & Flask-Mail, we imported all the required packages. 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json


#2. Opening the file📂 in readmode📑 to access the config.json file we created. 
with open('X:\Desktop_Reloaded\F2_WebDevolpment Projects\Python_MasterClass_RoadMap\Flask\\7_Sending Emails & Configurable Parameters In Flask\config.json', 'r') as c:
    params = json.load(c)["params"]

#3. keeping the local server parameter as true as we are currently on the local server.
local_server = "True"
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD =  params['gmail-password']
)

#4. Accessing the Database📁🗃 via URI (Every Database Software has a different URI. For examples. the URI for MYSQL, SQLlite, MongoDB etc will be all different from each other).
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

#5. Creating a class for the Contact📞 page's form.
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(20), nullable=False)

#6. Routing➡ the pages and URL's to their desired locations.
#a) Home page routing
@app.route('/')
def home():
    return render_template('index.html', params=params)

#b) about page routing
@app.route('/about')
def about():
    return render_template('about.html', params=params)

#c) contact page routing
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
            
        mail.send_message(
        'New message from ' + name,
        sender = email,
        recipients = [params['email-recipients']],
        body = f'''
Name - {name}
Phone no. - {phone} 
Email Id - {email}
Message - {message}'''
        )
    return render_template('contact.html', params=params)

#d) services page routing   
@app.route('/services.html')
def services():
    return render_template('services.html', params=params)


#e)🔴NOTE :- This is the most important thing to run our application which is not even mentioned in the official documentation of flask.
app.run(debug=True)