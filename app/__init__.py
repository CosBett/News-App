from ensurepip import bootstrap
from flask import Flask
from config import DevConfig
from flask_bootstrap5 import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)

# Creating the app configurations
  app.config.from_object(config_options[config_name])

  # Initializing flask extensions
  bootstrap.init_app(app)

# # App initialization
# app = Flask(__name__)
