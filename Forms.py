from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField, PasswordField
from flask_wtf import *
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password',[validators.length(min=5,max=15),validators.data_required()])

class CreateStaffForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    # role = RadioField('Role', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])

class logininformation(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])

class DocumentUploadForm(Form):
    Name = StringField('Name', validators=[DataRequired()])
    Comment = StringField('Comment', validators=[DataRequired()])
    Image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

