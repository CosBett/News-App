import os

class config:
  '''
  General configuration parent class
  '''
  
  NEWS_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}' 
  NEWS_HIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  NEWS_EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  NEWS_HIGHLIGHT_API_KEY = os.environ.get('NEWS_HIGHLIGHT_API_KEY')


class ProdConfig(config):
  '''
  Production configuration child class
  args:
       Config: the parent configuration class with General configuration settings
  '''


class DevConfig(config):
  '''
  Development configuration child class
  args: 
        config: the parent configuration class with General configuration settings
  '''

  Debug = True

  config_options = {
    'development': DevConfig,
    'production': ProdConfig,
  }