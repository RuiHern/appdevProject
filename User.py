# User class
class User:
    count_id = 0

    # initializer method
    def __init__(self, first_name, last_name,email,password):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password


    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return  self.__email
    def get_password(self):
        return  self.__password
    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self,email):
        self.__email = email
    def set_password(self,password):
        self.__password = password

class logincheck:
    def __init__(self, email2, password2):
        User.count_id += 1
        # , email2, password2
        self.__email2 = email2
        self.__password2 = password2
        # self.__email2 = "awdawda"
        # self.__password2 = "awdwadaada"

    def logincheckfunc(self):
        print("it means its works!!!!! you hear that yishun~~!!!!!!!! bob")

    def logincheckfunc2(self):
        print("it means its works!!!!! you hear that yishun~~!!!!!!!! bob22222222")

    def email_get(self):
        return self.__email2

    def password_get(self):
        return self.__password2

    def email_set(self):
        pass


class blog(User):
    def __init__(self, Name, Comment, File):
        User.count_id += 1
        self.__name = Name
        self.__comment = Comment
        self.__file = File

    def get_Name(self):
        return self.__name

    def get_Comment(self):
        return self.__comment

    def get_File(self):
        return self.__file

    def set_name(self, name):
        if name is not None:
            self.__name = name
        else:
            print("Invalid name provided.")

    def set_comment(self, comment):
        self.__comment = comment

    def set_file(self, file):
        self.__file = file


