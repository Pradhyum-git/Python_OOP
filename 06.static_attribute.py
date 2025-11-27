'''
1)Static/Class Attributes :
        An attribute shared by all objects of a class.
        Only one copy is created at class level
    Where it is defined ?
        Inside the class outside any method
2)Instance Attribute :
        An attribute that belongs to each object of a class
        Each object gets it's own separate copy.
    Where it is defined ?
        Inside the constructor(__init__ method) , they are created.
'''

class User :
    # Static Attribute : commonly shared for all objects of a User class
    user_count = 0
    
    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count+=1
    
    def display_user_details(self):
        print(f'Username : {self.username} /n Email : {self.email}')

user1=User('Pradhyum','cha@gmail.com')
user2=User('Pranitha','cha1@gmail.com')
user1.display_user_details()

# Accessing static attribute 
# 1) Using Class we can access static attribute
print('Accessing static attribute using Class: ',User.user_count)

# 2) Using Instance , we can access 
print('Accessing static attribute using user1 object: ',user1.user_count)
print('Accessing static attribute using user1 object: ',user2.user_count)
#Both Gives same result , because static attribute is same for all objects of a class