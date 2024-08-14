from Employee import Employee


class Manager(Employee):
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender, max_employees, employees=None):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender)
        self.max_employees = max_employees
        if employees is None:
            employees = []
        self.employees = employees[:self.max_employees]

    def print_employees(self):
        if self.employees:
            print(f'Employees list of manager: {self.firstname}, {self.lastname}:')
            for employee in self.employees:
                print(employee)
        else:
            print(f'There are no employees yet for manager: {self.firstname}, {self.lastname}:')

    def add_employee(self, employee):
        if len(self.employees) < self.max_employees and employee not in self.employees:
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
