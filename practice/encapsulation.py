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