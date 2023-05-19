from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    credential = field.data
    user = User.query.filter(
        (User.email == credential) | (User.username == credential)).first()
    if not user:
        raise ValidationError('provided credentials not found')


def password_matches(form, field):
    # Checking if password matches
    password = field.data
    credential = form.data['credential']
    user = User.query.filter(
        (User.email == credential) | (User.username == credential)).first()
    if not user:
        # raise ValidationError('no such user exists')
        return
    if not user.check_password(password):
        raise ValidationError('password was incorrect')


class LoginForm(FlaskForm):
    credential = StringField('credential', validators=[
                             DataRequired("must submit email or username"), user_exists])
    password = StringField('password', validators=[
                           DataRequired("must submit password"), password_matches])
