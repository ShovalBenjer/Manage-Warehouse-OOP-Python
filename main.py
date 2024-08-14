from Employee import Employee
from Manage import Manage
from Manager import Manager
from Menu import Menu
from Product import Product
from Warehouse import Warehouse
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


def print_products(manage):
    manage.print_products()


def print_employees(manage):
    manage.print_employees()


def print_managers(manage):
    manage.print_managers()


def add_new_product(manage):
    name = input('insert product name: ')
    description = input('insert product description: ')
    quantity = int(input('insert product quantity: '))
    location = input('insert product location: ')

    product = Product(name, description, quantity, location)
    if manage.add_product(product):
        print(f'product added!')
    else:
        print(f'failed to add product, Try again!')


def remove_product(manage):
    sku = input('insert product sku: ')

    if manage.remove_product(sku):
        print(f'{sku} deleted!')
    else:
        print(f'{sku} not exist!')


def add_new_employee(manage):
    e_id = input('insert employee id: ')
    firstname = input('insert firstname: ')
    lastname = input('insert lastname: ')
    phone_number = input('insert phone number in format 05X-XXXXXXX: ')
    address = input('insert address: ')
    gender = input('insert gender F/M: ')

    employee = Employee(e_id, firstname, lastname, phone_number, address, gender)
    if manage.add_employee(employee):
        print(f'employee added!')
    else:
        print(f'failed to add employee, Try again!')


def remove_employee(manage):
    cid = input('insert employee id: ')

    if manage.remove_employee(cid):
        print(f'{cid} deleted!')
    else:
        print(f'{cid} not exist!')


def convert_employee_to_manager(manage):
    e_id = input('insert employee id: ')
    max_employees = int(input('insert max employees for this manager: '))
    if manage.convert_employee_to_manager(e_id, max_employees):
        print(f'convert employee to be manager succeed')
    else:
        print(f'failed to convert employee to be manager, Try again!')


def add_employee_to_manager(manage):
    e_id = input('insert employee id: ')
    employee = manage.get_employee(e_id)
    m_id = input('insert manager id: ')
    manager = manage.get_employee(m_id)
    if isinstance(manager, Manager) and manager.add_employee(employee):
        print(f'employee added to manager!')
    else:
        print(f'failed to add employee to manager, Try again!')


def remove_employee_from_manager(manage):
    e_id = input('insert employee id: ')
    m_id = input('insert manager id: ')
    manager = manage.get_employee(m_id)
    if isinstance(manager, Manager) and manager.remove_employee(e_id):
        print(f'{e_id} removed from manager employees!')
    else:
        print(f'failed to remove {e_id} from manager employees')


def print_products_order_by_location(manage):
    manage.warehouse.print_products_order_by_location()


def print_products_by_location(manage):
    print('Exist Locations:\n', manage.warehouse.get_all_locations())
    location = input('Enter location: ')
    manage.warehouse.print_products_by_location(location)


def print_employees_of_manager(manage):
    manage.print_managers()
    manager_id = input('choose manager id: ')
    manage.print_employees_of_manager(manager_id)


def print_free_employees(manage):
    manage.print_free_employees()


def print_max_quantity_product(manage):
    manage.warehouse.print_max_quantity_product()


def print_min_quantity_location(manage):
    manage.warehouse.print_min_quantity_location()


def print_sum_quantity_of_all_locations(manage):
    manage.warehouse.print_sum_quantity_of_all_locations()


def exit_menu():
    print('Exiting program...')
    exit()


def main():
    products = get_products()
    employees = get_employees()
    warehouse = Warehouse(products)
    manage = Manage(warehouse, employees)
    manage.convert_employee_to_manager('666128965', 4)
    manage.convert_employee_to_manager('991004688', 4)

    menu_options = [
        ('Print all products in warehouse', print_products, manage),
        ('Print all employees', print_employees, manage),
        ('Print all managers', print_managers, manage),
        ('Add new product to the warehouse', add_new_product, manage),
        ('Remove product from warehouse', remove_product, manage,),
        ('Add new employee', add_new_employee, manage),
        ('Remove employee', remove_employee, manage),
        ('Make employee to be manager', convert_employee_to_manager, manage),
        ('Add employee to manager', add_employee_to_manager, manage),
        ('Remove employee from manager', remove_employee_from_manager, manage),
        ('Print all products by location', print_products_order_by_location, manage),
        ('Print all product for location', print_products_by_location, manage),
        ('Print all employees that belong to manager', print_employees_of_manager, manage),
        ('Print all employees that not belong to any manager', print_free_employees, manage),
        ('Print product with maximum quantity', print_max_quantity_product, manage),
        ('Print location with minimum quantity', print_min_quantity_location, manage),
        ('Print sum quantity for all locations', print_sum_quantity_of_all_locations, manage),
        ('EXIT', exit_menu, None),
    ]
    menu = Menu(menu_options)
    while True:
        menu.show()


if __name__ == '__main__':
    main()
