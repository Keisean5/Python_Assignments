# The BankAccount class should have a balance.
# When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0.
# The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. 
# (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

    # deposit(self, amount) - increases the account balance by the given amount
    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    # display_account_info(self) - print to the console: eg. "Balance: $100"
    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class User:
    def __init__(self, name, email, init_rate, balance):
        self.name = name
        self.email = email
        self.account = BankAccount(init_rate, balance)
    


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate/100
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'deposited {amount}')
        return self

    def withdraw(self, amount):
        print(f'withdrew {amount}')
        if self.balance < amount:
            print('Insufficient funds')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print(f'Insufficient Funds')
            self.balance -= 5
        else:
            self.balance += self.balance*self.int_rate
            return self
    
    def display_account_info(self):
        if self.balance == 0:
            print(f'0')
        else:
            print(f'Balance: {self.balance}')
        return self
    


sean = User ('Sean', 'ss@gmail.com', 0, 0)
sean.account = BankAccount(0,100)
print(sean.name, sean.email)
sean.account.deposit(0).withdraw(100).yield_interest().display_account_info()





# checking = BankAccount(0.01, 500)
# savings = BankAccount(0.02, 150)

# checking.deposit(100).deposit(30).deposit(60).withdraw(200).display_account_info()

# savings.deposit(300).deposit(30).withdraw(60).withdraw(200).yield_interest().display_account_info()





# sean = BankAccount (1, 100)
# sean.deposit(100)
# sean.withdraw(20)
# sean.yield_interest()
# print(f'Sean has {sean.balance} in their account.')
# print('-------------------------------------------')
# nate = BankAccount (1, 10)
# nate.withdraw(20)
# nate.yield_interest()
# print(f'Nate has {nate.balance} in their account.')
