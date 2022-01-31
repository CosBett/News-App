from nis import cat
from turtle import title
from unicodedata import category
import urllib.request, json
from .models import Articles, Source, TopHeadlines 

# Obtaining API key
api_key = None

# Obtaining base url
base_url = None

# Obtaining headlines url
headlines_url = None

# Obtaining everything url
everything_url = None

def configure_request(app):
  global api_key, base_url, headlines_url, everything_url
  api_key = app. config['NEWS_HIGHLIGHT_API_KEY']
  base_url = app.config['NEWS_HIGHLIGHT_API_BASE_URL']
  headlines_url = app.config['NEWS_HEADLINES_URL']
  everything_url = app.config['NEWS_EVERYTHING_URL']

def get_sources():
  '''
  This function gets the json response to our url request
  '''
  get_sources_url = base_url.__format__(api_key)
  with urllib.request.urlopen(get_sources_url) as url:
       get_sources_data = url.read()
       get_sources_response = json.loads(get_sources_data)

       source_results = None

       if get_sources_response ['results']:
         source_results_list = get_sources_response['results']
         source_results = process_source_results(source_results_list)

         return source_results
def  process_source_results(source_list):
  ''' 
  Function to proccess the source  results and tranform to a list of Objects

  args:
  source_list:  A list of dictionaries that contain sources details

  Returns:
  source_results: A list of source objects
  '''
  source_results = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.ge('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Source(id, name, description, url, category, language, country)
    source_results.append(source_object) 


def get_articles(source) :
  get_topHeadlines_url = headlines_url.format(source, api_key)

  with urllib.request.urlopen(get_topHeadlines_url) as url :
    topHeadlines_data = url.read()
    topHeadlines_response = json.loads(topHeadlines_data)

    topHeadlines_results = None 

    if topHeadlines_response['articles'] :
      topHeadlines_results_list = topHeadlines_response['articles']
      topHeadlines_results = process_topHeadlines_results(topHeadlines_results_list)

  return(topHeadlines_results)

def process_topHeadlines_results(topHeadlines_results_list) :
  '''
  process Top_headlines results and transform them to a list of objects
  '''
  topHeadlines_results = []
  for topHeadlines_item in topHeadlines_results_list :

    author = topHeadlines_item.get('author')
    title = topHeadlines_item.get('title')
    description = topHeadlines_item.get('description')
    url = topHeadlines_item.get('url')
    urlToImage = topHeadlines_item.get('urlToImage')
    publishedAt = topHeadlines_item.get('publishedAt')
    content = topHeadlines_item.get('content')

    topHeadlines_object = TopHeadlines(author, title, description, url, urlToImage, publishedAt, content)
    topHeadlines_results.append(topHeadlines_object)

  return topHeadlines_results
