class Calculator:
    # def __init__(self):
    #     pass
    
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y): 
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

obj1 = Calculator()

while True:
    print("\nOptions:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice = input("Select an operation from 1-5: ")
    
    if choice == "5":
        print("Choose from 1-4")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {obj1.add(num1, num2)}")
                
            elif choice == '2':
                print(f"Result: {obj1.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {obj1.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {obj1.divide(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please select a valid option.")
        
##Private calculator
        
class Calculator:
    
    def __add(self, x, y):  # Private method
        return x + y
    
    def __subtract(self, x, y):  # Private method
        return x - y
    
    def __multiply(self, x, y):  # Private method
        return x * y
    
    def __divide(self, x, y):  # Private method
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def calculate(self, operation, x, y):
        if operation == '1':
            return self.__add(x, y)
        elif operation == '2':
            return self.__subtract(x, y)
        elif operation == '3':
            return self.__multiply(x, y)
        elif operation == '4':
            return self.__divide(x, y)
        else:
            return "Invalid operation."

# Create an instance of the Calculator class
obj1 = Calculator()

# Loop for user input
while True:
    print("\nOptions:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice = input("Select an operation from 1-5: ")
    
    # Exit the loop if the user selects option 5
    if choice == "5":
        print("Exiting...")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = obj1.calculate(choice, num1, num2)
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please select a valid option.")
