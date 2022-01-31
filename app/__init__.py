from flask import Flask
from config import config_options
from flask_bootstrap5 import Bootstrap
from .main import main as main_blueprint

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

#registering the blueprint
  app.register_blueprint(main_blueprint)
# # App initialization
# app = Flask(__name__)
  return app