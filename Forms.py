from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField, PasswordField

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password',[validators.length(min=5,max=15),validators.data_required()])

class CreateStaffForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])

class logininformation(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])