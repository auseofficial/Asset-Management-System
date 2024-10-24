class Parent:
    def __init__(self, name, fathername):
        self.name = name
        self.fathername = fathername
    
    def details(self):
        print("Name:", self.name, "Father's Name:", self.fathername)

obj1 = Parent("Eshan", "Abu Taher")

obj1.details()