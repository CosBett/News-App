import urllib.request, json
from .models import Articles, Source

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
         