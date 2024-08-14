class Product:
    SKU_COUNTER = 0

    def __init__(self, name, description, quantity, location):
        Product.SKU_COUNTER += 1
        self.sku = f'PROD{Product.SKU_COUNTER}'
        self.name = name
        self.description = description
        self.quantity = quantity
        self.location = location

    def __str__(self):
        return f'{self.sku}, {self.name}, {self.description}, {self.quantity}, {self.location}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name

