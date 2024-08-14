# 319037404
# In this project each Class (Product,Employee,Warehouse,Manage) are in a separated file.
# data_utils for validate functions.
# data.py is the lists that was handed and I used import as needed for each file with max efficiency.
# Every feature should work as tested and debugged.
# No sign of .csv use needed.

from data import products_details, employees_details
from Product import Product
from Employee import Employee
from Warehouse import Warehouse
from Manage import Manage

# Create a list of products from the given list.
products = [Product(*product) for product in products_details]

# Create a list of employees from the given list.
employees = [Employee(*employee) for employee in employees_details]

# Create a warehouse object with the list of products.
warehouse = Warehouse(products)

# Create a management object with the list of employees and the warehouse object.
management = Manage(warehouse, employees)

# Print to the screen a menu for the user, press 9 to exit.
while True:
    print("Please choose an option:")
    print("1. Print the list of products in the warehouse.")
    print("2. Print the list of employees.")
    print("3. Add a new product.")
    print("4. Delete a product.")
    print("5. Add a new employee.")
    print("6. Delete an employee.")
    print("7. Print all products sorted by location.")
    print("8. Display the products in a certain location.")
    print("9. Exit the program.")
    choice = input("Enter your choice: \n")

    if choice == "1":
        management.print_products()
    elif choice == "2":
        management.print_employees()
    elif choice == "3":
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        quantity = input("Enter product quantity: ")
        location = input("Enter product location: ")
        new_product = Product(name, description, quantity, location)
        warehouse.add_product(new_product)
        print("Product added successfully.")
    elif choice == "4":
        sku = input("Enter product sku: ")
        if warehouse.remove_product(sku):
            print("Product removed successfully.")
        else:
            print("Product not found.")
    elif choice == "5":
        e_id = input("Enter employee ID: ")
        firstname = input("Enter employee first name: ")
        lastname = input("Enter employee last name: ")
        address = input("Enter employee address: ")
        phone = input("Enter employee phone number (optional): ")
        gender = input("Enter employee gender (optional): ")
        new_employee = Employee(e_id, firstname, lastname, address, phone, gender)
        management.add_employee(new_employee)
        print("Employee added successfully.")
    elif choice == "6":
        e_id = input("Enter employee ID: ")
        employee_to_remove = None
        for employee in employees:
            if employee.e_id == e_id:
                employee_to_remove = employee
                break
        if employee_to_remove:
            management.remove_employee(employee_to_remove)
            print("Employee removed successfully.")
        else:
            print("Employee not found.")
    elif choice == "7":
        warehouse.print_products_order_by_location()
    elif choice == "8":
        location = input("Enter location: ")
        warehouse.print_products_by_location(location)
    elif choice == "9":
        print("Bye Bye")
        break
    else:
        print("Invalid choice. Please try again.")
