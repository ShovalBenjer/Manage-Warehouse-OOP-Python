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
        id = row[0]
        firstname = row[1]
        lastname = row[2]
        phone = row[3]
        address = row[4]
        gender = row[5]
        l1.append([id, firstname, lastname, phone, address, gender])
    return l1


def valid_phone(phone_number: str):
    numbers = phone_number.split('-')
    if len(numbers) == 2 and len(str(numbers[0])) == 3 and numbers[0][:2] == '05' \
            and numbers[0].isdigit() and len(str(numbers[1])) == 7 and numbers[1].isdigit():
        return phone_number


def valid_gender(gender: str):
    if gender == 'M' or gender == 'F':
        return gender
