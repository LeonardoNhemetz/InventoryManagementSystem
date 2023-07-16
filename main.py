import mysql.connector

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database_name'
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        create_query = """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INT NOT NULL
            )
        """
        self.cursor.execute(create_query)
        self.connection.commit()

    def add_product(self, product):
        query = "INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
        values = (product.name, product.description, product.price, product.quantity)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_inventory(self, product_name, sold_quantity):
        query = "UPDATE products SET quantity = quantity - %s WHERE name = %s"
        values = (sold_quantity, product_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def check_inventory(self, product_name):
        query = "SELECT * FROM products WHERE name = %s"
        values = (product_name,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            name, description, price, quantity = result
            return Product(name, description, price, quantity)
        else:
            return None

    def generate_report(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        for result in results:
            name, description, price, quantity = result
            product = Product(name, description, price, quantity)
            print(f"Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

    def issue_alert(self, threshold):
        query = "SELECT * FROM products WHERE quantity < %s"
        values = (threshold,)
        self.cursor.execute(query, values)
        results = self.cursor.fetchall()

        for result in results:
            name, description, price, quantity = result
            print(f"Alert: Low inventory for product {name}!")

if __name__ == "__main__":
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
