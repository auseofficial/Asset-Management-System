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
  
