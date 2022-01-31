
class config:
  '''
  General configuration parent class
  '''
  pass

class ProdConfig(config):
  '''
  Production configuration child class
  args:
       Config: the parent configuration class with General configuration setings
  '''
  pass

class DevConfig(config):
  '''
  Development configuration child class
  args: 
        config: Theparent configuration with general configuration settings
  '''

  Debug = True