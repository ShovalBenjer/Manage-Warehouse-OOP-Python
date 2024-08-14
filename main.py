from Employee import Employee
from Manage import Manage
from Product import Product
from Warehouse import Warehouse
from App import App
from data_utils import read_products_csv_file, read_employees_csv_file


def get_products():
    products_details = read_products_csv_file()
    products = []
    for item in products_details:
        product = Product(item[0], item[1], item[2], item[3])
        products.append(product)
    return products


def get_employees():
    employees_details = read_employees_csv_file()
    employees = []
    for item in employees_details:
        employee = Employee(item[0], item[1], item[2], item[3], item[4], item[5])
        employees.append(employee)
    return employees


def main():
    products = get_products()
    employees = get_employees()
    warehouse = Warehouse(products)
    manage = Manage(warehouse, employees)
    managers = {
        '040436719': ['670208073', '976070029', '125931469', '880494554'],
        '529664732': ['756089454', '639372465', '666209465'],
        '524042850': ['657709986', '259542132', '623947496'],
        '557313954': ['378873020', '403402878', '285240784', '425545415']}
    # set managers
    for m, v in managers.items():
        manage.convert_employee_to_manager(m, 4)
        manager = manage.get_employee(m)
        for e in v:
            manager.add_employee(manage.get_employee(e))

    app = App(manage)
    app.show()


if __name__ == '__main__':
    main()
