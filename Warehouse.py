from Product import Product


class Warehouse:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def __str__(self):
        return "Warehouse class\nProducts:\n" + "\n".join(str(product) for product in self.products)

    def __repr__(self):
        return "Warehouse class\nProducts:\n" + "\n".join(str(product) for product in self.products)

    def add_product(self, product):
        if not isinstance(product, Product):
            return False
        self.products.append(product)
        return True

    def remove_product(self, sku):
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                return True
        return False

    def get_all_locations(self):
        locations = set()
        for product in self.products:
            locations.add(product.location)
        return ",".join(locations)

    def print_products_order_by_location(self):
        # Get unique locations from products list
        unique_locations = list(set([product.location for product in self.products]))

        # Sort locations alphabetically
        unique_locations.sort()

        # Iterate through locations and print products for each location
        for location in unique_locations:
            print("Location {}:".format(location))
            for product in self.products:
                if product.location == location:
                    print("\t{}, {}".format(product.name, product.quantity))

    def print_products_by_location(self, location):
        print("Products in location {}:".format(location))
        for product in self.products:
            if product.location == location:
                print(product.name + ", " + str(product.quantity))
