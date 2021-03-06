#!/var/www/cherry-pi-prod/venv

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp



class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
	access_key = HiddenField("Access Key")
	firstname = StringField('Firstname', validators=[DataRequired(), Length(min=1, max=20)])
	lastname = StringField('Lastname', validators=[DataRequired(), Length(min=0, max=30)])
	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


class SPPortalLoginForm(FlaskForm):
	spl_form_type = HiddenField()
	spl_email = StringField('Username or Email', validators=[DataRequired()])
	spl_password = PasswordField('Password', validators=[DataRequired()])
	spl_submit = SubmitField('Login')


class SPPortalRegister(FlaskForm):
	spr_form_type = HiddenField()
	spr_signup_key = StringField('Signup Key', validators=[DataRequired(), Length(min=16, max=16)], render_kw={"placeholder": "Invite Code"})
	spr_firstname = StringField('Firstname', validators=[DataRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Firstname"})
	spr_lastname = StringField('Lastname', validators=[DataRequired(), Length(min=0, max=30)], render_kw={"placeholder": "Lastname"})
	spr_username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)], render_kw={"placeholder": "Username"})
	spr_email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	spr_password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
	spr_confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
	spr_submit = SubmitField('Register')


class SPUploadForm(FlaskForm):
	upload_code = StringField('Upload Code', validators=[DataRequired()])
	file = FileField()
	submit = SubmitField('Upload')
