from flask_wtf import FlaskForm
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import RadioField, TextAreaField, validators
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField, PasswordField
from wtforms.validators import DataRequired


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])


class CreateStaffForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    role = RadioField('Role', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])


class logininformation(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])


class DocumentUploadForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Comment = StringField('Comment', validators=[DataRequired()])
    file = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')


class CreateProject(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = StringField('Phone', [validators.Length(min=8), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    address = StringField('House address', [validators.Length(min=1, max=150), validators.DataRequired()])
    house_type = RadioField('House Type', choices=[('AP', 'Appartment'), ('BUN', 'Bungalow'), ('HDB2', '2-Room HDB'),
                                                   ('HDB3', '3-Room HDB'),('HDB4', '4-Room HDB'),('HDB5', '5-Room HDB')
                                                   ,('CON', 'Condominium'), validators.DataRequired()])
    house_theme = RadioField('House Theme', choices=[('Scandanavian'), ('Luxury'), ('Modern-Luxury'),
                                                   ('Traditional'), ('Contemporary'),
                                                   ('Farmhouse'), ('CON', 'Condominium'), validators.DataRequired()])
    house_images = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    comments = TextAreaField('Additional Request', [validators.Optional()])

