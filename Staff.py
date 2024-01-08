import User

class Staff(User.User):
    count_id = 0

    def __init__(self, first_name, last_name,email,password):
        Staff.count_id += 1
        self.__staff_id = Staff.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    # accessor methods
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_password(self):
        return self.__password
    def get_staff_id(self):
        return self.__staff_id
    def get_email(self):
        return self.__email


    # mutator methods
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id
    def set_first_name(self,firstname):
        self.__first_name = firstname
    def set_last_name(self,last_name):
        self.__last_name = last_name
    def set_email(self, email):
        self.__email = email
    def set_password(self,password):
        self.__password = password


