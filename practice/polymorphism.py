class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Moving on")
        
class Car(Vehicle):
    def move(self):
        print("Moving the car") 
 
class Boat(Vehicle):
    def move(self): 
        print("Sailing the boat")                  
       
class Plane(Vehicle):
    def move(self):
        print("flying  the plane")     
        
car1=Car("Ford","Lambo")
boat1=Boat("Joshim","abahoni")           
plane1=Plane("US Bangla","Biman")

for x in (car1,boat1,plane1):
 print(x.brand)
 print(x.model)
 x.move()
 
 #Example2
 
class Boy:
     def __init__(self,name,age):
         self.name=name
         self.age=age
         
     def info(self):
         print(f"My name is :{self.name}") 
         
     def gender(self):
         print("Male")  
         
class Girl:
     def __init__(self,name,age):
         self.name=name
         self.age=age
         
     def info(self):
         print(f"My name is :{self.name}") 
         
     def gender(self):
         print("Female")     
         
boy1=Boy("Eshan",25)
girl=Girl("gal",23)

for person in (boy1,girl):
  person.gender()
  person.info() 
  person.gender()
 
#Example3 

from math import pi  

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
        
    def area(self):
        return self.length * self.width
        
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
      
    def area(self):
        return pi * self.radius * self.radius

                
rectangle1 = Rectangle("Rec", 5, 3)  
circle1 = Circle("Cir", 5)        

print(f"Here is the output: The area of {rectangle1.name} is {rectangle1.area()}")
print(f"The area of the {circle1.name} is: {circle1.area()}")