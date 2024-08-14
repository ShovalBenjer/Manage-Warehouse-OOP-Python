class Product:
    sku_counter = 0

    def __init__(self, name, description, quantity, location):
        Product.sku_counter += 1
        self.sku = f"PROD{Product.sku_counter}"
        self.name = name
        self.description = description
        self.quantity = quantity
        self.location = location

    def __str__(self):
        return f"{self.sku}, {self.name}, {self.description}, {self.quantity}, {self.location}"

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.quantity}, '{self.location}')"
