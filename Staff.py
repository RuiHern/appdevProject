import User

class Staff(User):
    count_id = 0

    def __init__(self, first_name, last_name, gender, membership, remarks, email, date_joined, address):
        super().__init__(first_name, last_name, gender, membership, remarks)
        Staff.count_id += 1
        self.__staff_id = Staff.count_id
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address

    # accessor methods
    def get_staff_id(self):
        return self.__staff_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    # mutator methods
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address


