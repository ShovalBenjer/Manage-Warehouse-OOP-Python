class Manage:
    def __init__(self, warehouse, employees=[]):
        self.warehouse = warehouse
        self.employees = employees

    def __str__(self):
        return "Manage class - Python OOP course - assignment"

    def __repr__(self):
        return "Manage class - Python OOP course - assignment"

    def add_product(self, product):
        self.warehouse.append(product)

    def remove_product(self, product):
        if product in self.warehouse:
            self.warehouse.remove(product)

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_products(self):
        print("Warehouse Products:")
        for product in self.warehouse.products:
            print(product)

    def print_employees(self):
        print("Warehouse Employees:")
        for employee in self.employees:
            print(employee)
