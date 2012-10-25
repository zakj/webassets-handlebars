from flask import Flask, render_template
from flask.ext.assets import Bundle, Environment


app = Flask(__name__)
app.config['ASSETS_DEBUG'] = True
assets = Environment(app)
assets.url = '/static'
assets.register(
    'templates',
    'vendor/handlebars.runtime-1.0.rc.1.js',
    Bundle(
        '*.handlebars',
        #depends='*.handlebars',
        filters='handlebars', output='handlebars.js'),
    output='templates.js')


@app.route('/')
def index():
    return render_template('index.html')
