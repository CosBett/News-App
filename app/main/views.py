from flask import render_template,request,redirect, url_for, jsonify
import json
from . import main
from ..requests import get_articles, get_sources,get_topHeadlines

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
# Obtaining News sources
  news_sources = get_sources()
  articles = get_articles()
  topHeadlines = get_topHeadlines()
  title = 'Home - Welcome to Worldwide News Website'
  return render_template('index.html', title = title, source_list = news_sources, articles = articles, top_headlines = topHeadlines)

@main.route('/source')
def source():
  '''
  View root page function that returns the index page and its data
  '''
# Obtaining News sources
  source = request.args.get("name")
  topHeadlines = get_topHeadlines()
  print('topHeadlines', topHeadlines)
  return render_template('source.html', title = 'this is sourcepage', source_list = topHeadlines)
  