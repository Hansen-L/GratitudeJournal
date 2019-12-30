from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title1 = StringField('First Entry Title', validators=[DataRequired()])
    title2 = StringField('Second Entry Title', validators=[DataRequired()])
    title3 = StringField('Third Entry Title', validators=[DataRequired()])
    content1 = TextAreaField('Content', validators=[DataRequired()])
    content2 = TextAreaField('Content', validators=[DataRequired()])
    content3 = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

