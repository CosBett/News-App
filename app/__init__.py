from flask import Flask
from config import config_options
from flask_bootstrap5 import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__,)

# Creating the app configurations
  app.config.from_object( config_options[config_name])

# Setting up configuration

  # # app.config.from_object(DevConfig)
  # app.config.from_pyfile('config.py')

  #Initializing flask extensions
  bootstrap.init_app(app)

# # App initialization
# app = Flask(__name__)
  return app