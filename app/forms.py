from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])

class SignUpForm(FlaskForm):
	firstname = StringField('First Name', validators=[InputRequired()])
	lastname = StringField('Last Name', validators=[InputRequired()])
	email = EmailField('Email', validators=[InputRequired(), Email()])
	age = IntegerField('Age', validators=[InputRequired()])
	gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], default=1)
	password = PasswordField('Password', validators=[InputRequired()])
	passwordConfirm = PasswordField('Confirm password', validators=[InputRequired()])