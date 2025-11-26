# Let's combine two objects with an example
class Dog: 
    # __init__ : It is a constructor used to instantiated while creating an object.
    # self : It is a parameter where object name is passed implicitly.
    def __init__(self,name,age,owner):
        # attributes
        self.name=name 
        self.age = age
        self.owner = owner
    
    # Methods 
    def bark(self):
        print("Bow-bow")

# Owner class
class Owner:
    def __init__(self,name,city,mobile_number):
        self.name = name
        self.city = city
        self.phone_number = mobile_number

owner1=Owner('Pradhyum','India',6309772978)
dog1=Dog('Tommy',21,owner1)
print(dog1.owner) # This is an instance of the Owner class stored at memory location 0x711c06763fd0"
print(owner1)
print(dog1.owner.name)

owner2=Owner('Vinay','Pune',983213458)
dog2=Dog('Tommy',21,owner2)
print(dog2.owner)
print(dog2.owner.name)