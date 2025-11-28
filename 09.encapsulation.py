'''
                        Encapsulation :
Encapsulation is the process of wrapping data (attributes) and methods (functions) 
into a single unit called a class, and restricting direct access to some parts of an object.

Key idea : Hides the data , show only which is necessary
Encapsulation allows you to control how data is accessed and modified using getter and setter methods.
'''

class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property 
    def balance(self):
        # getter method is used to get the balance using property decorator
        return self.__balance
    
    def deposit(self,amount):
        if(amount<=0):
            raise ValueError("Amount should be positive")
        else:
            self.__balance+=amount
    
    def withdraw(self,amount):
        if(amount> self.__balance):
            raise ValueError("Insufficient Funds")
        else:
            self.__balance -= amount

account1 = BankAccount()
print("Balance: ",account1.balance) # using property decorator we are accessing getter method like attribute value
amount = int(input("Enter amount to deposit: "))
account1.deposit(amount) # raises error when amount is less than or equal to 0
print("Balance: ",account1.balance) 
amount = int(input("Enter amount to withdraw: "))
account1.withdraw(amount) # raises error when amount is greater than existing balance
print("Balance: ",account1.balance) 