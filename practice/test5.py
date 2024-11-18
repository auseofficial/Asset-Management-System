# OOP 
# -Inheritance 
# -Encapsulation
# -Abstraction
# -Polymorphism


# Inheritence

class Animal:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        
class Dog(Animal):
    def __init__(self,color):
        self.color=color
        
obj1=Animal("RoToiler","Black")    
obj2=Dog("Black")            
print(obj1.name)
print(obj2.color)


#Encapsulation

class Bank:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.__account_number=account_number
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance+=amount     
    
    def remaining(self):
        return self.__balance
    
obj1=Bank("Akib",12345678,4500)
print(obj1.remaining())