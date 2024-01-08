from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm, CreateStaffForm , logininformation
import shelve, Staff
from db import *
from User import *

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/createStaff', methods=['GET', 'POST'])
def create_staff():
    create_staff_form = CreateStaffForm(request.form)
    if request.method == 'POST' and create_staff_form.validate():
        staff = Staff(create_staff_form.first_name.data,create_staff_form.last_name.data,create_staff_form.gender.data,create_staff_form.email.data,create_staff_form.date_joined.data,create_staff_form.address.data,create_staff_form.membership.data,create_staff_form.remarks.data,create_staff_form.password.data )
        add_staff(staff)
        print(staff.get_first_name(), staff.get_last_name(), "was stored in staff.db successfully with user_id ==",
              staff.get_staff_id())

        return redirect(url_for('retrieveStaff'))
    return render_template('createStaff.html', form=create_staff_form)

@app.route('/retrieveStaff')
def retrieveStaff():
    staff_dict = {}
    db = shelve.open('staff.db', 'r')
    staff_dict = db['staff']
    db.close()

    staff_list = []
    for key in staff_dict:
        staff = staff_dict.get(key)
        staff_list.append(staff)

    return render_template('retrieveStaff.html', count=len(staff_list), users_list=staff_list)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # create_login_form = logininformation(request.form)
    # if request.method == 'POST' and create_login_form.validate():
    #     check = logincheck(create_login_form.email2.data,create_login_form.password2.data)
    #     check.logincheckfunc2()
    #
    # else:
    #     check = logincheck(create_login_form.email2.data, create_login_form.password2.data)
    #     check.logincheckfunc()
    # return render_template('login.html', form=create_login_form)
    create_login_form = logininformation(request.form)
    if request.method == 'POST' and create_login_form.validate():
        customer = logincheck(logininformation.email.data, logininformation.password.data)
        customer.email_set(logininformation.email.data)
        print(customer.email_get())

    return render_template('login.html', form=create_login_form)



@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        customer = User(create_user_form.first_name.data, create_user_form.last_name.data,create_user_form.email.data,create_user_form.password.data)
        add_user(customer)
        print(customer.get_first_name(), customer.get_last_name(), "was stored in customer.db successfully with user_id ==",
              customer.get_user_id())

        return redirect(url_for('retrieveCustomers'))
    return render_template('createCustomer.html', form=create_user_form)

@app.route('/retrieveCustomers')
def retrieveCustomers():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveCustomers.html', count=len(users_list), users_list=users_list)
@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def deleteCustomer(id):
    users_dict = {}
    db = shelve.open('user.db','w')
    users_dict = db['Users']
    users_dict.pop(id)
    db['Users'] = users_dict
    db.close()
    return redirect(url_for('retrieveCustomers'))

@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_email(update_user_form.email.data)
        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieveCustomers'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.email.data = user.get_email()
        update_user_form.password.data = user.get_password()

        return render_template('updateCustomer.html', form=update_user_form)
# @app.route('login')
# def login():
#

@app.route('/CreateForum.html', methods=['GET', 'POST'])
def CreateForum():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()



if __name__ == '__main__':
    app.run(debug=True)

