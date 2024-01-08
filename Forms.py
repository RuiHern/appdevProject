from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField, PasswordField

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password',[validators.length(min=5,max=15),validators.data_required()])

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class logininformation(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])


class createProject(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = StringField('Phone', [validators.Length(min = 8), validators.DataRequired()])
    house_type = RadioField('House Type', choices=[('AP','Appartment'), ('BUN', 'Bungalow'), ('HDB2', '2-Room HDB'),
                                                   ('HDB3', '3-Room HDB'),('HDB4', '4-Room HDB'),('HDB5', '5-Room HDB')
                                                   ,('CON', 'Condominium'), validators.DataRequired()])
    address = StringField('House address', [validators.Length(min=1, max=150), validators.DataRequired()])
    postal_code = StringField('Postal', [validators.Length(min=1, max=150), validators.DataRequired()])


    house_theme = RadioField('House Type', choices=[('AP', 'Appartment'), ('BUN', 'Bungalow'), ('HDB2', '2-Room HDB'),
                                                   ('HDB3', '3-Room HDB'), ('HDB4', '4-Room HDB'),
                                                   ('HDB5', '5-Room HDB')
        , ('CON', 'Condominium'), validators.DataRequired()])
    add_comment = TextAreaField('Remarks', [validators.Optional()])