'''
                         Getter and Setter Methods 

Getter : A method used to access the value of private variable / attribute
Setter : A method used to modify the value of private attribute safely.

Why are they used ?
Because , direct accessing of object data might be risky
1)Data integrity
2)Validating values before updated
3) Preventing unauthorized changes
4)Achieving encapsulation


'''
from datetime import datetime
import re
class User:
    def __init__(self,name,email,password):
        self.username = name
        self.__email = email
        self.__password = password 
    
    def get_email(self):
        print("Email accessed at ",datetime.now())
        return self.__email
    def set_email(self,email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            print("Email updated")
            self.__email = email
        else:
            print('Invalid Email')

user1 = User('Pradhyum','chavalapradhyum@gmail.com','Apee')
# access the private variable using getter method
print(user1.get_email())

# modify the email
user1.set_email('ch1913@gma') # not validated 
print(user1.get_email())

user1.set_email('chakri1913@gma.com')
print(user1.get_email())

'''
When they are used?

Use getters and setters when:

1)Data must be protected from direct modification

2)You want to validate data before updating

3)You need controlled access to class attributes

4)Attributes are private (prefixed with __ in Python)

'''

'''
                            Property Decorators
Property Decorators is a elegant way to write getter and  setter methods in python
'''

class User:
    def __init__(self,name,email,password):
        self.username = name
        self._email = email
        self.__password = password 
    
    # @property : This decorator make easy to getter method without explicitly calling , use it like a normal attribute.
    @property
    def email(self):
        print("Email accessed at ",datetime.now())
        return self._email
    # @attribute.setter : This decorator is used to call setter method using like attribute
    @email.setter
    def email(self,email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            print("Email updated")
            self._email = email
        else:
            print('Invalid Email')

user1 = User('Pradhyum','chavalpranitha@gmail.com','Apee')
print(user1.email) # This implicitly calls getter method
user1.email = 'prani12@gmail.com'
print(user1.email)

# the setter decorator must start with the same name as the attribute