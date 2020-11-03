import flask_wtf
import wtforms
from wtforms import validators as vld

class SignupForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign up")

class AlbumForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name of song:", validators=[vld.DataRequired()])
    source = wtforms.StringField("Source of song:", validators=[vld.DataRequired()])
    category= wtforms.StringField("Category of song:", validators=[vld.DataRequired()])
    submit = wtforms.SubmitField("upload song")


class MessageForm(flask_wtf.FlaskForm):
    name_of_sender = wtforms.StringField("Name of sender:", validators=[vld.DataRequired()])
    subject_of_message = wtforms.StringField("Subject of message:", validators=[vld.DataRequired()])
    source_of_video= wtforms.StringField("Source of video:", validators=[vld.DataRequired()])
    submit = wtforms.SubmitField("send a message to admin")


class SigninForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign in")

class QueryForm(flask_wtf.FlaskForm):
    query    = wtforms.StringField("")
    submit   = wtforms.SubmitField("Search")
