# User class
import shelve
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

class Project(User):
    def __init__(self, first_name, last_name, email, phone,address, house_type, house_images, house_theme, comments, password):
        super().__init__(first_name, last_name, email)
        self.__phone = phone
        self.__house_type = house_type
        self.__house_theme = house_theme
        self.__house_images = house_images
        self.__address = address
        self.__comments = comments

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def get_house_type(self):
        return self.__house_type

    def get_house_theme(self):
        return self.__house_theme

    def get_house_images(self):
        return self.__house_images
    def get_comments(self):
        return self.__comments

    def set_phone(self,phone):
        self.__phone = phone
    
    def set_address(self,address):
         self.__address = address
    
    def set_house_type(self,house_type):
        self.__house_type = house_type
    
    def set_house_image(self,house_images):
        self.__house_images = house_images

    def set_house_theme(self,house_theme):
         self.__house_theme = house_theme

    def set_comments(self,comments):
         self.__comments = comments