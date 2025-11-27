'''
1)Static Methods :
        Static Methods belong to class but does not uses object and class variables.
        - Doesn't use self keyword as parameter.
        Static Method = No self, no cls → does not depend on object or class data
    How it is created?
        Using @staticmethod decorator , static methods are created.
    Why it is used ?
        - Logical Grouping : Functions that are related to class but not uses class and object variables for calculation
        - Utility Functions

    When it is Used ?
        The method does not depend on instance or class attributes
        You want utility/helper functions inside class

''' 


class Voter:
    nationality = 'Indian'

    def __init__(self,name,state):
        self.name = name
        self.state = state
    
    def voter_details(self):
        print(f"Voter Name: {self.name} and state: {self.state}")

    @staticmethod
    def is_valid_for_voting(age):
        # This method doesn't need 'self' because it doesn't use name or state.
        #In this method we are not using class / instance variable .
        return age>=18

voter1=Voter('Pradhyum','AP')

# accessing the static method is done using class
# accessing also can done using object , but through class is prefarble
print(Voter.is_valid_for_voting(19))
print(voter1.is_valid_for_voting(19))  # works, but not recommended
print(Voter.is_valid_for_voting(16))

# Static Method not equals to class attribute