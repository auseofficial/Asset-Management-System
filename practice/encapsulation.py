class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    # Method to check balance (read-only access)
    def get_balance(self):
        return self.__balance


# Creating an account
account = BankAccount("Akib Us Suny Eshan", 1000)

# Using public methods to access the private balance
print(f"Initial Balance: ${account.get_balance()}")
account.deposit(500)
print(f"Balance after deposit: ${account.get_balance()}")
account.withdraw(300)
print(f"Balance after withdrawal: ${account.get_balance()}")

# Accessing the private balance directly (not recommended, but possible)
print(f"Direct access to balance: ${account._BankAccount__balance}")


class Bankaccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.__balance = balance  # Private attribute
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Corrected from `+-` to `+=`
            print(f"Deposit Successful: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Corrected condition
            self.__balance -= amount  # Corrected from `+-` to `-=`
            print(f"Withdrawal Successful: ${amount}")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    def get_balance(self):
        return self.__balance


# Creating an account
obj1 = Bankaccount("Akib Us Suny Eshan", 10000, "xxxxyyyy89")

# Using methods to test the output
print(f"Initial Balance: ${obj1.get_balance()}")
obj1.deposit(500)
print(f"Balance after deposit: ${obj1.get_balance()}")
obj1.withdraw(300)
print(f"Balance after withdrawal: ${obj1.get_balance()}")

# Accessing the private balance directly (not recommended, but possible)
print(f"Direct access to balance: ${obj1._Bankaccount__balance}")



###2nd example

class Bank:
    def __init__(self,holder_name,balance):
     self.holder_name=holder_name
     self.__balance=balance
     
    def deposit(self,amount):
         self.__balance += amount
         
    def get_balance(self):
         return self.__balance 
     
obj1 = Bank("Eshan",10000)
obj1.deposit(1000000)
print(f"Here is the final balance: ${obj1.get_balance()}")

class DBBL:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance +=amount
        
    def remaining_balance(self):
        return self.__balance
    
obj1=DBBL("Akib",10000)
obj1.deposit(100000)
print(obj1.remaining_balance())    
obj1.name="Eshan"
print(obj1.name)    


#3rd example

class Brac:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance += amount

    def remaining (self):
        return self.__balance    
        
obj1= Brac("Akib",10000)
obj1.name="Suny"
print(obj1.name)
print(obj1.remaining())        
        
               