from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Message', validators=[InputRequired()])
