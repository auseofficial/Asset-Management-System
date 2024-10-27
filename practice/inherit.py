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

class Phone:
    def __init__(self,brand,color,ram):
        self.brand=brand
        self.color=color
        self.ram=ram
        
    def run(self):
        return (f"Whats the brand ? {self.brand}") 
    
obj1=Phone("Apple","Black","HundredGB")
print(obj1.run())

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
 