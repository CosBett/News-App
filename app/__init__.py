from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap5 import Bootstrap

bootstrap = Bootstrap()

# App initialization
app = Flask(__name__)
