from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def home():
    return 'Hello, World!'

@app1.route('/about')
def about():
    return 'About'

#pushthis