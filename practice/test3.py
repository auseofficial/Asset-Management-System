class DBBL:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        initial_balance = self.__balance
        if amount > self.__balance:
            return "Insufficient Balance"
        else:
            self.__balance -= amount
            return f"This is your balance: {initial_balance}\nYou have withdrawn: {amount}\nNow your balance is: {self.__balance}"

obj1 = DBBL("Akib", 12345, 1000)
obj1.deposit(0)          
print(obj1.withdraw(1001))     
