'''
Access Modifiers : Mechanisms used in Object-Oriented Programming to control access to class attributes and methods.
They decide who can access or modify data in a class.

1)Public - Accessible anywhere.
2)Protected - Accessible within the class and subclass 
3)Private - Accessible only within the class - can't accesss and can't modify outside the class.

'''

class User:
    def __init__(self,name,email,password):
        self.username = name
        self._email = email # protected attribute
        self.__password = password # private attribute

user1 = User('Pradhyum','pradhyum@2005','AP22Prad')
# can access the protected attribute but should not use outside the class it is like naming convention
# Python developer should follow : 
#                  We are all consenting adults here.
# So we should not use protected varibale it is meant for internal use.
print(user1._email) 

user1._email = 'char'
print(user1._email)
try:
    print(user1.__password)
except Exception as e:
    print(e)