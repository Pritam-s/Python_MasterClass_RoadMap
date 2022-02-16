from flask import Flask, render_template

app = Flask(__name__)

#Home 
@app.route("/")
def home():
    name = "Pritam Singh"
    return render_template('index.html', display_name = name)

#About 
@app.route("/about")
def about():
    return render_template('about.html')


app.run(debug=True)