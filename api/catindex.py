from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'It"s Big Cat!'

@app.route('/about')
def about():
    return 'About'
