# на Отлично в одного человека надо сделать консольное приложение 
# Телефонный справочник с внешним хранилищем информации, 
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление.

# Задача 38: Дополнить телефонный справочник  возможностью 
# изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

# для отлично в группах надо выполнить или ТГ бот или ГУИ
# (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД

# ГУИ можно сделать просто на EasyGUI или Tkinter

import json

def load_all_contacts():
    with open("phonebook.json", "r", encoding="utf-8") as phonebook_json:
        return json.load(phonebook_json)

def save_changes(contacts_to_save):
    with open("phonebook.json", "w", encoding="utf-8") as phonebook_json:
        phonebook_json.write(json.dumps(phonebook, ensure_ascii=False))
    with open("phonebook.json", "r", encoding="utf-8") as phonebook_json:
        contacts_to_save = json.load(phonebook_json)
    return contacts_to_save

def add_contact(contacts_to_supplement):
    name = input("Input name:")
    if name in contacts_to_supplement:
        print("Contact already exists")
        return

    contacts_to_supplement[name] = {}
    city = input("Input city: ")
    contacts_to_supplement[name]["city"] = city
    birthday = input("Input birthday date: ")
    contacts_to_supplement[name]["birthday"] = birthday
    contacts_to_supplement[name]["phone_numbers"] = []
    input_phone = input("Input phone number: ")
    contacts_to_supplement[name]["phone_numbers"].append(input_phone)
    while input_phone != 'stop':
        input_phone = input("Input another phone number(if any). Input 'stop' if there are no other phone numbers: ")
        if input_phone != 'stop':
            contacts_to_supplement[name]["phone_numbers"].append(input_phone)
    save_changes(contacts_to_supplement)
    print("You successfully added a new contact!")
    return contacts_to_supplement
    

def show_all_contacts():
    print(load_all_contacts())

def edit_contact(contacts_to_edit):
    contact_to_edit = input('Input the name of the contact you want to edit: ')
    del contacts_to_edit[contact_to_edit]
    name = input('Input new name of the contact: ')
    contacts_to_edit[name] = {}
    city = input("Input new city: ")
    contacts_to_edit[name]["city"] = city
    birthday = input("Input new birthday date: ")
    contacts_to_edit[name]["birthday"] = birthday
    contacts_to_edit[name]["phone_numbers"] = []
    input_phone = input("Input new phone number: ")
    contacts_to_edit[name]["phone_numbers"].append(input_phone)
    while input_phone != 'stop':
        input_phone = input("Input another new phone number(if any). Input 'stop' if there are no other phone numbers: ")
        if input_phone != 'stop':
            contacts_to_edit[name]["phone_numbers"].append(input_phone)
    save_changes(contacts_to_edit)
    print(f'You successfully edited the contact!')
    return contacts_to_edit

def remove_contact(contacts_to_remove_in):
    contact_to_remove = input('Input the name of the contact you want to remove: ')
    del contacts_to_remove_in[contact_to_remove]
    save_changes(contacts_to_remove_in)
    print('You successfully removed the contact')
    return contacts_to_remove_in

def find_contact(contacts_to_find_in):
    contact_to_find = input("Input name, city, birthday date, or phone number to find a contact: ")
    contact_found = False
    for i in iter(contacts_to_find_in):
        if contact_to_find in i:
            contact_found = True
            print(f'Contact found: {i}, {contacts_to_find_in[i]}')
        else:
            for j in contacts_to_find_in[i].values():
                if contact_to_find in j:
                    contact_found = True
                    print(f'Contact found: {i}, {contacts_to_find_in[i]}')
    if contact_found == False:
        print('There are no contacts satisfying your request.')


phonebook = {"Дядя Петя": {"city": "Moscow", "birthday": "01.01.1994", "phone_numbers": ["12345", "12346"]} }

while True:
    phonebook = load_all_contacts()
    command = input("Input your command:")
    if command == "/start":
        print("Welcome to your contact list!")
    elif command == "/stop":
        save_changes(phonebook)
        print("You closed your contact list. Bye!")
        break
    elif command == "/all":
        show_all_contacts()
    elif command == "/add":
        add_contact(phonebook)
    elif command == "/edit":
        edit_contact(phonebook)
    elif command == "/remove":
        remove_contact(phonebook)
    elif command == "/find":
        find_contact(phonebook)
    else:
        print('Input error. Try again.')
