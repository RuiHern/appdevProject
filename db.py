from User import User
import shelve
def get_key(my_dict):
    if len(my_dict)==0:
        my_key = 1
    else:
        my_key = max(my_dict.keys()) + 1
    return my_key
def add_user(user):
    users_dict = {}
    db = shelve.open('user.db', 'c')
    try:
        users_dict = db['Users']
    except:
        print("Error in retrieving Users from user.db.")

    user.set_user_id(get_key(users_dict))
    users_dict[user.get_user_id()] = user
    db['Users'] = users_dict
    # Test codes
    db.close()

def display_allUsers():
    users_dict = {}
    db = shelve.open('user.db', 'c')
    try:
        users_dict = db['Users']
        for k,v in users_dict.items():
            print(v)
    except:
        print("Error in retrieving Users from user.db.")


def save_user(user):
    users_dict = {}
    db = shelve.open('user.db', 'c')
    try:
        users_dict = db['Users']
    except:
        print("Error in retrieving Users from user.db.")
    db['Users'] = users_dict
    db.close()
def save_customer(customer):
    customers_dict = {}
    db = shelve.open('customer.db', 'c')
    try:
        customers_dict = db['Customers']
    except:
        print("Error in retrieving Customers from customer.db.")
    customers_dict[customer.get_user_id()] = customer
    db['Customers'] = customers_dict
    db.close()
if __name__ == '__main__':
    display_allUsers()