from flask import Flask
from config import DevConfig
from flask_bootstrap5 import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)

# Creating the app configurations
  app.config.from_object( DevConfig )

# Setting up configuration

  app.config.from_object(DevConfig)
  app.config.from_pyfile('config.py')
  
  # Initializing flask extensions
  # bootstrap.init_app(app)

# # App initialization
# app = Flask(__name__)
