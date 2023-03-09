from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        for p in self.phones:
            if p == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for p in self.phones:
            if p == old_phone:
                p == new_phone


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
