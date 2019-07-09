from flask import render_template
from MyApp import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'mukunda'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool !'

        }
    ]
    return render_template('index.html', title='Home', user=user, post=posts)
