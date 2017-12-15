# all the imports
import os
from flask import Flask
# from flask , request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import Api

app = Flask(__name__)  # create the application instance :)
api = Api(app)  # create the api object which helps in restful framework
app.config.from_object(__name__)  # load config from this file

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

