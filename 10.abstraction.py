'''
                Abstraction : 
    Abstraction is the process of showing only essential things and hiding the unnecessary details from the user.
    It mainly focuses on what an object does rather than how it does it.
    - Hide complexity and expose only the required functionality.


Example : A person wants to withdraw money
You press : Withdraw -> Enter PIN -> Enter amount -> collect cash
You don't how it atm validates you card , how atm connects to your bank server , how it check your balance , how it counts cash
All these complex implementation is hidden.
'''
class BankAccount:
    def __init__(self,username,balance=1000):
        self._balance = balance
        self.username = username

    def check_balance(self):
        return self._balance
    
    def withdraw(self,amount):
        if(self.check_balance()):
            print("Withdraw successfull")
            self._balance -= amount
        else:
            print('Insufficient funds')

account1 = BankAccount('Pradhyum')
print('Balance: ',account1.check_balance())
account1.withdraw(500)
print('Balance: ',account1.check_balance())

'''
In this example
you are just withdrawing money 
you don't how they are checking money and how they updating balance after withdraw
'''

# another example of email 
class Email:
    def _connect(self):
        print("Connecting to email server")
    
    def _authenticate(self):
        print("Authenticating")
    
    def send_email(self):
        self._connect()
        self._authenticate()
        print('Sending Email')
        self._disconnect()
    
    def _disconnect(self):
        print("Disconnecting to email server")

email = Email()
email.send_email()

'''
From this example you don't know how an email is connecting and authenticating ,sending and disconnecting
you are just sending message

'''
