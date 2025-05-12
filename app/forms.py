from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit =  SubmitField("Sign in")
    remember_me = BooleanField("Remember Me")

class RecipeForm(FlaskForm):
    title        = StringField('Title', validators=[DataRequired()])
    ingredients  = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    tags         = StringField('Tags (comma-separated)', validators=[Optional()])
    submit       = SubmitField('Save')
