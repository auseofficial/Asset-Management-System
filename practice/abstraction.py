from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def eat(self):
        print("I am eating banana")
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.catrgory="Monkey"
        self.name=name
        super().__init__()
        
    def eat(self):
        print("Kola khai")    
        
obj1=Monkey("Lucky")        
obj1.eat()           
              
              
#Example2              
                          
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
    
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")

class Square(Polygon):
    def noofsides(self):
        print("I have 4 sides")

# Creating instances and calling the methods
obj1 = Triangle()
obj1.noofsides()

obj2 = Square()
obj2.noofsides()

# class Calculator:
#     def __init__(self):
#         pass

#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Error! Division by zero."
#         return a / b

# # Create an instance of Calculator
# calc = Calculator()

# # User input loop
# while True:
#     print("\nOptions:")
#     print("1: Add")
#     print("2: Subtract")
#     print("3: Multiply")
#     print("4: Divide")
#     print("5: Exit")

#     choice = input("Select an operation (1/2/3/4/5): ")

#     if choice == '5':
#         print("Exiting...")
#         break

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))

#             if choice == '1':
#                 print(f"Result: {calc.add(num1, num2)}")
#             elif choice == '2':
#                 print(f"Result: {calc.subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"Result: {calc.multiply(num1, num2)}")
#             elif choice == '4':
#                 print(f"Result: {calc.divide(num1, num2)}")

#         except ValueError:
#             print("Invalid input. Please enter a number.")
#     else:
#         print("Invalid choice. Please select a valid option.")
