from flask import render_template,request,redirect, url_for
import app
from . import main
from ..requests import get_sources


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #  Obtaining News sources
    news_sources = get_sources()
    print(news_sources)

    title = 'Home - Welcome to Worldwide News Website'
    return render_template('index.html', title = title, sources = news_sources)