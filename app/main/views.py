from flask import render_template,request,redirect, url_for
from . import main
from ..requests import get_articles, get_sources,get_topHeadlines

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #  Obtaining News sources
    news_sources = get_sources()
    articles = get_articles()
    topHeadlines = get_topHeadlines()
    print(news_sources)


    title = 'Home - Welcome to Worldwide News Website'
    return render_template('index.html', title = title, news_sources = news_sources, articles = articles, topHeadlines = topHeadlines)