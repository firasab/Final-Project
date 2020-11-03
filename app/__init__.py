import flask
from config import Config
from config import Config_users

app = flask.Flask(__name__) # __name__ is the name of the folder

app.config.from_object(Config)


from . import views
