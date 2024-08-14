from data_utils import validate_phone_number, validate_gender


class Employee:
    def __init__(self, e_id, firstname, lastname, address, phone=None, gender=None):
        if not all([e_id, firstname, lastname, address]):
            raise ValueError("All required fields must be provided")
        self.e_id = e_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = f"{firstname.lower()}.{lastname.lower()}@email.com"
        self.address = address
        self.phone_number = validate_phone_number(phone) if phone else None
        self.gender = validate_gender(gender) if gender else None

    def __str__(self):
        return f"{self.e_id}, {self.firstname}, {self.lastname}, {self.email}," \
               f" {self.address}, {self.phone_number}, {self.gender}"

    def __repr__(self):
        return str(self)
