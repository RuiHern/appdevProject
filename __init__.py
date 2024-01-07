from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm, CreateCustomerForm
import shelve, User, Staff

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,create_user_form.email.data,create_user_form.password.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db.close()

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
    # else:
    #     users_dict = {}
    #     db = shelve.open('user.db', 'r')
    #     users_dict = db['Users']
    #     db.close()
    #     user = users_dict.get(id)
    #     update_user_form.first_name.data = user.get_first_name()
    #     update_user_form.last_name.data = user.get_last_name()
    #
    #     return render_template('updateCustomer.html', form=update_user_form)

if __name__ == '__main__':
    app.run(debug=True)

