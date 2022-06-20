from collections import UserDict
dict = {}

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    ...

class Phone(Field):
    ...

class Record:

    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []

        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone, new_tel):
        for i, phone in enumerate(self.phones):
            if self.phones[i].value == phone.value:
                self.phones[i] = new_tel

    def remove_phone(self, phone):
        for i, phone in enumerate(self.phones):
            if phone.value == phone.value:
                self.phones.pop(i)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record




if __name__ == '__main__':
    print('Перевірка роботи класу Record')
    name1 = Name('Andrij')
    tel1 = Phone('+380970000000')
    record = Record(name1, tel1)
    record.change_phone(tel1, Phone('+38(098)111 11 11'))
    record.add_phone(Phone('+380973333333'))
    print(record.name.value)
    print(record.phones[0].value)
    print(record.phones[1].value)
    print('----------------------------------------------------')
    print('перевірка роботи класу Addressbook')
    book1 = AddressBook()
    book1.add_record(record)
    #print(book1)
    for x in book1.data['Andrij'].phones:
        print(x.value)
    for y in book1.data:
        print(y)
    print('----------------------------------------------------')
    print('Перевірка додавання наступних даних')
    name2 = Name('Marta')
    tel2 = Phone('0984556200')
    record2 = Record(name2, tel2)
    record2.add_phone(Phone('050-111-11-11'))
    book1.add_record(record2)
    #print(book1.data)
    for i in book1.data['Marta'].phones:
        print(i.value)
    for n in book1.data:
        print(n)

