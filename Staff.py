import User

class Staff(User.User):
    count_id = 0

    def __init__(self, first_name, last_name,email, address,password):
        super().__init__(first_name,last_name,email)
        Staff.count_id += 1
        self.__staff_id = Staff.count_id
        self.__email = email
        self.__address = address
        # self.__staffrole = staffrole
        self.__password = password

    # accessor methods
    def get_password(self):
        return self.__password
    def get_staff_role(self):
        return self.__staffrole
    def get_staff_id(self):
        return self.__staff_id

    def get_email(self):
        return self.__email


    def get_address(self):
        return self.__address

    # mutator methods
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_email(self, email):
        self.__email = email


    def set_address(self, address):
        self.__address = address

    def set_staff_role(self,staffrole):
        self.__staffrole = staffrole
    def set_password(self,password):
        self.__password = password


