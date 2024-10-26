#Single Inheritance

class Abba:
    bike="Hero Honda"
    taka="1000Crore"
    home="10 floor"
    
class Pola(Abba):    
    bike="Royal Enfield"
    taka="1lakh"
    
v=Pola()
print(v.bike)    


# Multiple Inheritance

class Abba:
    bike="Hero Honda"
    taka="1000Crore"
    home="10 floor"

class Kaka:
    bike="Pulsar"
    taka="1Crore"
    home="1st floor"
    
class Nana:
    bike="R15"
    taka="100Crore"
    home="8 floor"
    
            
class Pola(Abba,Kaka,Nana):    
    bike="Royal Enfield"
    taka="1lakh"
    home=Nana.home
    
v= Nana()
print(v.home)

#Multilevel Inheritance

class Abba:
    bike="Hero Honda"
    taka="1000Crore"
    home="10 floor"

class Kaka(Abba):
    bike="Pulsar"
    taka="1Crore"
    home="1st floor"
    
class Nana(Kaka):
    bike="R15"
    taka="100Crore"
    home="8 floor"
    
            
class Pola(Nana):    
    bike="Royal Enfield"
    taka="1lakh"
    home=Nana.home
    
v=Pola()
print(v.bike)

# Hybrid And Hierarchical Inheritance

class Abba:
    def __init__(self, bike, taka, home):
        self.bike = bike
        self.taka = taka
        self.home = home

class Kaka(Abba):
    def __init__(self, bike, taka, home):
        super().__init__(bike, taka, home)

class Nana(Kaka):
    def __init__(self, bike, taka, home):
        super().__init__(bike, taka, home)

class Pola(Nana):
    def __init__(self, bike, taka, home):
        super().__init__(bike, taka, home)

kakar = Kaka("Pulsar", "1 Crore", "1st floor")
nanar = Nana("R15", "100 Crore", "8th floor")
polar = Pola("Royal Enfield", "1 Lakh", nanar.home)

print(f"Kakar bike: {kakar.bike}") 
print(f"Nanar  bike: {nanar.bike}")   
print(f"Polar bike: {polar.bike}")

#Practice

class Akib:
    def __init__(self,Education,Designation,Office):   
     self.Education=Education
     self.Designation=Designation
     self.Office=Office
class Efty(Akib):     
    def __init__(self,Education,Designation,Office):   
      super().__init__(Education,Designation,Office)
class Nadim(Efty):    
    def __init__(self,Education,Designation,Office):   
       super().__init__(Education,Designation,Office)

Boss1=Akib("JU","Software Engineer","WALTON")
Boss2=Efty("DMC","Medical Student","Dhaka")
Boss3=Nadim("BAU","Agri Student","Mymensingh")       
          
print(Boss1.Designation)      
print(Boss2.Office)
print(Boss3.Education)


class Animal:
    def __init__(self,eyes,legs):
        self.eyes=eyes
        self.legs=legs
    def details(self):
        print(f"Eyes :{self.legs}") 
           
obj1=Animal("black","white")
print(obj1.legs)


# Create a base class Person with attributes name and age, and a method display_info that prints these details. 
# Then, create a derived class Student that inherits from Person and adds an 
# additional attribute grade. Override the display_info method in Student to include the grade when displaying information.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age) 
        self.grade = grade  

    def display_info(self):

        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


obj1 = Person("Akib Us Suny Eshan", 25)
obj2 = Student("Akib Us Suny Eshan", 25, "A")

print(obj1.name) 
print(obj1.age) 
print(obj2.grade)

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

