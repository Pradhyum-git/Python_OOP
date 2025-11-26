'''
Object-Oriented Programming is a programming approach that organizes software design around objects rather than functions.

Objects represent real-world entities (like Car, Student, Bank Account) and contain:
Data → attributes / variables
Behavior → methods / functions

Terminologies used in oop.
Class : A blueprint of an object.
Object : Instance of a class.
Method : Function inside a class.
Attribute : Variable inside a class.
Constructor : A special type of method instantieted while creating an object.
'''

# creation of class : using class keyword class is created with classname
# Syntax : class class_name:
class Dog: 
    # __init__ : It is a constructor used to instantiated while creating an object.
    # self : It is a parameter where object name is passed implicitly.
    def __init__(self,name,age):
        # attributes
        self.name=name 
        self.age = age
    
    # Methods 
    def bark(self):
        print("Bow-bow")

# object creation
dog1=Dog('Tommy',21)
print(type(dog1))
print('Name of the dog is',dog1.name)
dog1.bark()

dog2=Dog('Tommy',21)
print(type(dog2))
print('Name of the dog is',dog2.name)
dog2.bark()