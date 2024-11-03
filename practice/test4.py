#inheritence

class Animal:
    def __init__(self,eat,hunt):
        self.eat=eat
        self.hunt=hunt
        
class Bird(Animal):
    def __init__(self,eat,hunt,fly):
        super().__init__(eat,hunt)
        self.fly=fly
        
obj1=Animal("Meat","They love hunting")
obj2=Bird("Meat","They love hunting","Yes the love to fly")
print(obj1.eat)
print(obj2.fly)


#Encapsulation

class DBBL:
    def __init__(self,account_number,balance,type):
        self.account_number=account_number
        self._balance=balance
        self.type=type
        
    def amount(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. Your current balance is: {self._balance}")
        elif self._balance >= abs(amount):
            self._balance -= abs(amount)
            print(f"Withdrew {abs(amount)}. Your remaining balance is: {self._balance}")
        else:
            print(f"Insufficient balance for withdrawal of {abs(amount)}")
            
obj1=DBBL(123456,10000,"Savings")
obj1.amount(2000)

#abstractmethod

from abc import ABC, abstractmethod

class Bear(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract methods should have no implementation

    @abstractmethod
    def move(self):
        pass

class Dog(Bear):
    def sound(self):
        return "Bark"

    def move(self):
        return "It can move"

# Instantiate Dog, which implements all abstract methods from Bear
obj2 = Dog()
print(obj2.sound())  # Output: Bark
print(obj2.move())   # Output: It can move


#polymorphism

from abc import ABC, abstractmethod

class Bear(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract methods should have no implementation

    @abstractmethod
    def move(self):
        pass

class Dog(Bear):
    def sound(self):
        return "Bark"

    def move(self):
        return "It runs quickly"

class Cat(Bear):
    def sound(self):
        return "Meow"

    def move(self):
        return "It walks gracefully"

# Polymorphic function
def animal_behaviour(animal):
    print(animal.sound())
    print(animal.move())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Test polymorphism
animal_behaviour(dog)  # Output: Bark, It runs quickly
animal_behaviour(cat)  # Output: Meow, It walks gracefully

from math import Pi
class Shape:
    def __init__(self,name)
     self.name=name
     
class Rectangle(Shape):
    def __init__(self,name)
     super().__init__(name)
     
     def area (self):
         return self.length * self.width

class Circle(Shape):
    def __init__(self,radius)
     self.radius=radius
    super().__init__(name)
         
    def area(self):
         return pi*self.radius*self.radius
         
         
         
from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius
    
# Example usage
rectangle = Rectangle("Rectangle", 5, 3)
circle = Circle("Circle", 4)

print(f"{rectangle.name} area: {rectangle.area()}")  # Rectangle area: 15
print(f"{circle.name} area: {circle.area()}")        # Circle area: 50.26548245743669

         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         








