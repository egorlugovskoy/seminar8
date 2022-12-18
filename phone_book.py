phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id):
    global phone_book
    name1 = phone_book[id - 1][0]
    name2 = phone_book[id - 1][1]
    name3 = phone_book[id - 1][2]
    print(name1 + name2 + name3)
    name1 = input('Измените Имя:')
    name2 = input('Измените номер телефона:')
    name3 = input('Измените коменнтарий:')
    confirm = input(f'Вы действительно хотите сохранить изменения? {name1}? (y/n)')
    if confirm.lower() == 'y':
        phone_book[id - 1][0] = name1
        phone_book[id - 1][1] = name2
        phone_book[id - 1][2] = name3
        return True
    return False

def find_contact(name):
    global phone_book
