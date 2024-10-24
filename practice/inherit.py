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


class Akib:
    def __init__(self,company,designation,duration):
     self.copmpany=company
     self.designation=designation
     self.duration=duration
     
obj1= Akib("WALTON","Software Engineer","Four Months")
print(obj1.duration)


class Animal:
    def __init__(self,eyes,legs):
        self.eyes=eyes
        self.legs=legs
obj=Animal("black","white")
print(obj.legs)        