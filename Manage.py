from Manager import Manager


class Manage:
    def __init__(self, warehouse, employees=None):
        if employees is None:
            employees = []
        self.employees = employees
        self.warehouse = warehouse

    def __str__(self):
        return 'Manage class - Python OOP course - assignment'

    def __repr__(self):
        return self.__str__()

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            return True
        return False

    def get_employee(self, e_id):
        for employee in self.employees:
            if employee.e_id == e_id:
                return employee

    def remove_employee(self, e_id):
        employee = self.get_employee(e_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def add_product(self, product):
        return self.warehouse.add_product(product)

    def remove_product(self, product):
        return self.warehouse.remove_product(product)

    def print_employees(self):
        print('Employees:')
        for e in self.employees:
            print(e)

    def print_products(self):
        print(self.warehouse)

    def convert_employee_to_manager(self, e_id, max_employees):
        e = self.get_employee(e_id)
        if e:
            index = self.employees.index(e)
            manager = Manager(e_id, e.firstname, e.lastname, e.phone_number, e.address, e.gender, max_employees)
            self.employees[index] = manager
            return True
        return False

    def get_managers(self):
        managers = []
        for e in self.employees:
            if isinstance(e, Manager):
                managers.append(e)
        return managers

    def print_managers(self):
        managers = self.get_managers()
        if managers:
            print('Managers:')
            for e in managers:
                print(e)
        else:
            print(f'There are no managers yet')

    def print_employees_of_manager(self, e_id):
        e = self.get_employee(e_id)
        if e and isinstance(e, Manager):
            e.print_employees()

    def print_free_employees(self):
        not_free_employee = []
        managers = self.get_managers()
        for m in managers:
            not_free_employee += m.employees
        for e in self.employees:
            if e not in not_free_employee:
                print(e)
