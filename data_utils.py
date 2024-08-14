import csv


def read_products_csv_file():
    l1 = []
    csv_file = open("products_list.csv")
    read = csv.reader(csv_file)
    for row in read:
        name = row[0]
        description = row[1]
        quantity = int(row[2])
        location = row[3]
        l1.append([name, description, quantity, location])
    return l1


def read_employees_csv_file():
    l1 = []
    csv_file = open("employees_list.csv")
    read = csv.reader(csv_file)
    for row in read:
        e_id = row[0]
        firstname = row[1]
        lastname = row[2]
        phone = row[3]
        address = row[4]
        gender = row[5]
        l1.append([e_id, firstname, lastname, phone, address, gender])
    return l1


def valid_phone(phone_number: str):
    numbers = phone_number.split('-')
    if len(numbers) == 2 and len(str(numbers[0])) == 3 and numbers[0][:2] == '05' \
            and numbers[0].isdigit() and len(str(numbers[1])) == 7 and numbers[1].isdigit():
        return phone_number


def valid_gender(gender: str):
    if gender == 'M' or gender == 'F':
        return gender


def employee_exception(employees, e_id):
    """
    Check if the employee with the given id is already in the list.
    :param employees: the list of employees.
    :param e_id: the id of the employee.
    :return: error message if the employee is already in the list, None otherwise.
    """
    for employee in employees:
        if employee.e_id == e_id:
            return f"Employee with ID '{e_id}' already exists."
    return None


def id_exception(id_number):
    # Ensure the input is of correct length and all digits
    if len(id_number) != 9 or not id_number.isdigit():
        return False

    # Initial calculation
    total_sum = 0
    weights = [1, 2, 1, 2, 1, 2, 1, 2]
    for i in range(8):
        digit = int(id_number[i])
        multiplied = digit * weights[i]

        # If the result of multiplication is a two-digit number, add its digits together
        if multiplied > 9:
            multiplied = sum(int(digit) for digit in str(multiplied))

        total_sum += multiplied

    # Calculate the check digit
    check_digit = (10 - total_sum % 10) % 10

    # Return True if the check digit matches the last digit of the ID, False otherwise
    return check_digit == int(id_number[-1])


def input_exception(input_value):
    """
    Check if input value is empty.
    :param input_value: the value of the input field.
    :return: error message if the value is empty, None otherwise.
    """
    if not input_value:
        return "This field must not be empty."
    return None


def phone_exception(phone_number: str):
    # Validate if phone_number is not None
    if phone_number is None:
        return "Phone number must not be None."

    # Validate the overall length
    if len(phone_number) != 11:
        return "Phone number must be 11 chars."

    numbers = phone_number.split('-')

    # Validate the split parts
    if len(numbers) != 2:
        return "Phone number must be separated by char '-' and include only 2 parts."

    prefix, number = numbers

    # Validate the prefix
    if len(prefix) != 3 or not prefix.isdigit() or prefix[:2] != '05':
        return "Phone prefix must start with '05' and have a total of 3 digits."

    # Validate the number part
    if len(number) != 7 or not number.isdigit():
        return "Phone number must include only numbers."

    # All conditions are satisfied
    return None
