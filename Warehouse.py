class Warehouse:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def __str__(self):
        s = 'Products:\n'
        for p in self.products:
            s += f'{p}\n'
        return s

    def __repr__(self):
        return self.__str__()

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            return True
        return False

    def remove_product(self, sku):
        for p in self.products:
            if p.sku == sku:
                self.products.remove(p)
                return True
        return False

    def get_all_locations(self):
        return ','.join(sorted(set(p.location for p in self.products)))

    def print_products_order_by_location(self):
        l1 = sorted(self.products, key=lambda pr: pr.location)
        location = None
        for p in l1:
            if location is None or location != p.location:
                print(f'Location {p.location}:')
                location = p.location
            print(f'\t{p.name}, {p.quantity}')

    def print_products_by_location(self, location):
        l1 = [p for p in self.products if p.location == location]
        print(f'Products in location {location}:')
        for p in l1:
            print(f'\t{p.name}, {p.quantity}')

    def print_max_quantity_product(self):
        product = max(self.products, key=lambda p: p.quantity)
        print(f'max quantity:', product)

    def print_min_quantity_location(self):
        grouped_products = {}
        for product in sorted(self.products, key=lambda p: p.location):
            grouped_products[product.location] = grouped_products.get(product.location, 0) + product.quantity
        min_quantity = None
        min_location = None
        print('Quantity for locations:')
        for location, quantity in grouped_products.items():
            if min_quantity is None:
                min_quantity = quantity
            elif quantity < min_quantity:
                min_quantity = quantity
                min_location = location
        print(f'location {min_location} with minimum quantity of {min_quantity} products')

    def print_sum_quantity_of_all_locations(self):
        grouped_products = {}
        for product in sorted(self.products, key=lambda p: p.location):
            grouped_products[product.location] = grouped_products.get(product.location, 0) + product.quantity
        print('Quantity for locations:')
        for location, quantity in grouped_products.items():
            print(f'{location}: {quantity} ')
