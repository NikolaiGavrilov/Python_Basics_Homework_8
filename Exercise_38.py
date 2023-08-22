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

def load_phonebook():
    with open("dishes.json", "r", encoding="utf-8") as phonebook_json:
        return json.load(phonebook_json)

def save_changes():
    with open("phonebook.json", "w", encoding="utf-8") as phonebook_json:
        phonebook_json.write(json.dumps(phonebook, ensure_ascii=False))

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
    print("You successfully added a new contact!")
    save_changes()

def show_all_contacts(contacts_to_show):
    print("Here is your full list of contacts:")
    print(contacts_to_show)

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
    save_changes()
    print(f'You successfully edited the contact!')

def remove_contact(contacts_to_remove_in):
    contact_to_remove = input('Input the name of the contact you want to remove: ')
    del contacts_to_remove_in[contact_to_remove]
    save_changes()
    print('You successfully removed the contact')

def find_contact(contacts_to_find_in):
    contact_to_find = input("Input name to find a contact: ")
    if contact_to_find in contacts_to_find_in:
        print(f"Contact was found! {contact_to_find}, {contacts_to_find_in[contact_to_find]} ")
    else:
        print('Contact was not found.')


phonebook = {"Дядя Петя": {"city": "Moscow", "birthday": "01.01.1994", "phone_numbers": ["12345", "12346"]} }

while True: 
    command = input("Input your command:")
    if command == "/start":
        print("Welcome to your contact list!")
    elif command == "/stop":
        save_changes()
        print("You closed your contact list. Bye!")
        break
    elif command == "/all":
        show_all_contacts(phonebook)
    elif command == "/add":
        add_contact(phonebook)
    elif command == "/edit":
        edit_contact(phonebook)
    elif command == "/remove":
        remove_contact(phonebook)
    elif command == "/find":
        find_contact(phonebook)
