class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_inventory(self, product_name, sold_quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity -= sold_quantity
                break

    def check_inventory(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def generate_report(self):
        for product in self.products:
            print(f"Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

    def issue_alert(self, threshold):
        for product in self.products:
            if product.quantity < threshold:
                print(f"Alert: Low inventory for product {product.name}!")


# Example usage of the inventory management system

inventory = Inventory()

# Adding products
product1 = Product("T-shirt", "White cotton t-shirt", 25.00, 50)
product2 = Product("Jeans", "Blue denim jeans", 60.00, 30)
product3 = Product("Cap", "Black cap with logo", 15.00, 10)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Updating inventory
inventory.update_inventory("T-shirt", 10)
inventory.update_inventory("Jeans", 5)

# Checking inventory
product_checked = inventory.check_inventory("T-shirt")
print(f"Product checked: {product_checked.name}, Quantity: {product_checked.quantity}")

# Generating inventory report
inventory.generate_report()

# Issuing low inventory alert
inventory.issue_alert(15)
