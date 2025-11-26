# In this script let's go to how to access and modify the attributes

# User class
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_another_user(self,user):
        print(f'Sending hi to {user.username}: Hi  {user.username} , Iam {self.username}')

user1 = User('Pradhyum','chavalapradhyum@gmail.com','Pradhyum@2005')
user2 = User('Viany','Vinay@gmail.com','Vinay2003')

# accessing the data
print(user1.username)
user1.say_hi_to_another_user(user2)

#modfying the data
user1.email = 'Pradhyum.com' # it is invalid for email
print(user1.email)
