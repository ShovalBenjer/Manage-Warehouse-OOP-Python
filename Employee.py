from data_utils import valid_phone, valid_gender
from Person import Person


class Employee(Person):
    def __init__(self, e_id, firstname, lastname, phone_number, address, gender):
        super().__init__(e_id, firstname, lastname)
        self.email = firstname + '.' + lastname + '@email.com'
        self.phone_number = valid_phone(phone_number)
        self.address = address
        self.gender = valid_gender(gender)

    def __str__(self):
        return f'{super().__str__()}, {self.email},' \
               f'  {self.phone_number}, {self.address},{self.gender} '

    def __repr__(self):
        return self.__str__()
