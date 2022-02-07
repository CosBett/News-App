from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from newsapi import NewsApiClient

def create_app(config_name):
  app = Flask(__name__,instance_relative_config=True)
  newsapi = NewsApiClient
# Creating the app configurations
  app.config.from_object(config_options[config_name])
  app.config.from_pyfile('config.py') 
#Initializing flask extensions
  Bootstrap(app)

#registering the blueprint
  from .main import main as main_blueprint

  app.register_blueprint(main_blueprint)
  
#setting config
  from .requests import configure_request
  configure_request(app)

# # App initialization
# app = Flask(__name__)
  return app

  