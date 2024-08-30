#appone

from flask import Flask

appone = Flask(__name__)

@appone.route('/')
def home():
    return 'It"s Big Cat!'

@appone.route('/about')
def about():
    return 'About'
