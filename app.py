from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/page')
def page():
    return "<h1>Nova Página</h1><br><a href=\"/\">Home</a>"