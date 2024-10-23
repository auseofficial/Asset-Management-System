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
    def __init__(self,bike,taka,home):
        self.bike=bike
        self.taka=taka
        self.home=home
class Kaka(Abba):
    def __init__(self,bike,taka,home):
         super().__init__(bike,taka,home)
class Nana(Kaka):
    def __init__(self,bike,taka,home):
        super().__init__(bike,taka,home) 
class Pola(Nana):
    def __init__(self,bike,taka,home):
        super().__init__(bike,taka,home)
        
Kaka=Kaka("Pulsar", "1 Crore", "1st floor") 
nana = Nana("R15", "100 Crore", "8th floor")
pola = Pola("Royal Enfield", "1 Lakh", nana.home)    
                        
print(Kaka.bike)
