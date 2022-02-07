from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class config:
  '''
  General configuration parent class
  '''
  
  NEWS_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}' 
  NEWS_HIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apikey={}'
  NEWS_EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  NEWS_HIGHLIGHT_API_KEY = environ.get('API_KEY')

# https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY

class ProdConfig(config):
  '''
  Production configuration child class
  args:
       Config: the parent configuration class with General configuration settings
  '''
  pass

class DevConfig(config):
  '''
  Development configuration child class
  args: 
        config: the parent configuration class with General configuration settings
  '''

  Debug = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}