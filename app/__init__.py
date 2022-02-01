from flask import Flask
from flask_bootstrap5 import Bootstrap
from config import config_options
from .main import main as main_blueprint
from .requests import configure_request


bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__,)

# Creating the app configurations
  app.config.from_object( config_options[config_name])

# Setting up configuration

#Initializing flask extensions
  bootstrap.init_app(app)

#registering the blueprint
  app.register_blueprint(main_blueprint)
  
#setting config
  configure_request(app)

# # App initialization
# app = Flask(__name__)
  return app