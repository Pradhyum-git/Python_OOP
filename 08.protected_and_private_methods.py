'''
Public Methods : We can access this methods from any where
Protected Method : This type of methods can access from class and it's subclass
Private Method : This type of methods can access only from it's class.

'''
# Let's see how an protected method accessed
class Animal:
    def _make_sound(self): # protected method
        print('Some sound')
class Dog(Animal):
    def bark(self):
        self._make_sound()
dog1=Dog()
dog1.bark()
dog1._make_sound() # possible , but not recommendad .

# Let's see how an private method works
class BankAccount:
    def __calculate_interest(self):
        print("Interest Calculated")

class PradhyumAccount(BankAccount):
    def calculate_interest(self):
        self.__calculate_interest() # gives error because private method is not accessed in the subclass

account = PradhyumAccount()
account.calculate_interest()

'''
Private attribute & methods names are mangled for safety , To prevent accidental access & accidental override in subclasses 
'''