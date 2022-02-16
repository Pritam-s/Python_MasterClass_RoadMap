# From the 'Flasks' official documentation.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>" 

app.run(debug=True) # app.run() is very important to be called. This is not included in the official documentation.

#(debug = True) - This is an argument which we can give in app.run(). We don't want to restart our app everytime we make changes so it is used to automatically restart the app.