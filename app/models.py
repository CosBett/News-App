class Articles:
  '''
  Articles class to define articles objects
  '''
  def __init__(self,source, author, title, description, url, urlToImage,publishedAt, content):
    self.source = source
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content

class Source:
  '''
  Source class to define source objects
  '''
  def __init__(self, id, name, description, url, category, language, country):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country
    
class TopHeadlines:
  ''' 
  live top and breaking headlines for a country, specific category in a country, single source, or multiple sources
  '''  
  def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
    self.id = id
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content
