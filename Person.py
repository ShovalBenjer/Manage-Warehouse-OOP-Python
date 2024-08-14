class Person:
    def __init__(self, e_id, firstname, lastname):
        if not e_id or not firstname or not lastname:
            raise ValueError("e_id, firstname and lastname must be non-empty.")
        self.e_id = e_id
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.__class__.__name__}: {self.e_id}, {self.firstname}, {self.lastname}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Person) and self.e_id == other.e_id
