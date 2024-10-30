class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def reduce_quantity(self, amount):
        if self.__quantity >= amount:
            self.__quantity -= amount
            return True
        else:
            return False


class Shop:
    def __init__(self):
        self.products = []  # List to store products

    def add_product(self, product):
        self.products.append(product)  # Add product to the list

    def display_products(self):
        print("\nAvailable Products and Quantities:")
        for index, product in enumerate(self.products, start=1):
            # Display each product with its index, name, price, and quantity
            print(f"{index}. {product.get_name()} - ${product.get_price()} - Quantity: {product.get_quantity()}")

    def buy_product(self, product_index, quantity):
        # Check if the product index is valid
        if 0 < product_index <= len(self.products):
            product = self.products[product_index - 1]  # Get the selected product
            if product.reduce_quantity(quantity):
                # If successful, print a success message
                print(f"\nCongratulations! You've successfully purchased {quantity} of {product.get_name()}.\n")
            else:
                # If insufficient quantity, print an error message
                print("\nSorry, insufficient quantity available.\n")
        else:
            # If invalid selection, print an error message
            print("\nInvalid product selection.\n")


# Initialize Shop and Products
shop = Shop()
shop.add_product(Product("Samsung", 10000, 3))
shop.add_product(Product("Vivo", 8000, 3))
shop.add_product(Product("Apple", 12000, 3))

# Display Menu and Interact
while True:
    shop.display_products()
    choice = int(input("\nEnter the number of the product to buy or 0 to exit: "))
    if choice == 0:
        print("Thank you for visiting our shop!")
        break
    quantity = int(input("Enter the quantity you want to buy: "))
    shop.buy_product(choice, quantity)