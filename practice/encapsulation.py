class Parent:
    def __init__(self, name, fathername):
        self.name = name
        self.fathername = fathername
    
    def details(self):
        print("Name:", self.name, "Father's Name:", self.fathername)

obj1 = Parent("Eshan", "Abu Taher")
obj2 = Parent("Mama", "Kaka")

obj1.details()
obj2.details()


class Car:
    def __init__(self,color):
        self.color=color
    
car1=Car("Blue")
print(car1.color)    

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

# Using public methods to access private balance
print(f"Initial Balance: ${account.get_balance()}")
account.deposit(500)
print(f"Balance after deposit: ${account.get_balance()}")
account.withdraw(300)
print(f"Balance after withdrawal: ${account.get_balance()}")

