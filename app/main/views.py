from flask import render_template
from app import app


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Worldwide News Website'
    return render_template('index.html', title = title)