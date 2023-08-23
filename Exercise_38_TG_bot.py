#Ссылка на бота: t.me/Phone_Book_Gavrilov_bot

import telebot
from random import *
import json
import requests

phonebook = ["Дядя Петя", "12346", "Тётя Таня", "202346"]

API_TOKEN='6594391523:AAFTGzLwGtadT87OLhQzIUlVRbMSkM5mX4A'
bot = telebot.TeleBot(API_TOKEN)

def load_all_contacts():
    with open("phonebook_TG.json", "r", encoding="utf-8") as phonebook_TG_json:
        return json.load(phonebook_TG_json)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome to your contact list!")
    bot.send_message(message.chat.id, "You can use following commands in this bot:\n /start - to launch the bot\n /stop - to stop the bot\n /all - to show all contacts in your phone book\n /add - to add new contact\n save - to save the progress you've achieved\n /phone - to learn the contact's phone by inputing his or her name\n /remove - to remove the contact from your list\n /editname - to change the contact's name\n /editphone - to change the contact's phone")
phonebook = load_all_contacts()

@bot.message_handler(commands=['stop'])
def start_message(message):
    bot.send_message(message.chat.id, "You closed your contact list. Bye!")

@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, "Here is your list of contacts: ")
    for i in range(len(phonebook)):
        if i%2 == 0:
            bot.send_message(message.chat.id, phonebook[i])

@bot.message_handler(commands=['add'])
def get_name(message):
    bot.send_message(message.chat.id, "Input name of the contact:")
    bot.register_next_step_handler(message, get_phone)
 
def get_phone(message):
    bot.send_message(message.chat.id, "Input phone of the contact:")
    user_data = {
        "name": message.text,
        "phone": None
    }
    bot.register_next_step_handler(message, create_message, user_data)
 
def create_message(message, user_data):
    user_data["phone"] = message.text
    name = user_data["name"]
    phone = user_data["phone"]
    phonebook.append(name)
    phonebook.append(phone)
    bot.send_message(message.chat.id, f"Contact {name} was successfully added.")

@bot.message_handler(commands=['save'])
def save_contacts(message):
    with open("phonebook_TG.json", "w", encoding="utf-8") as phonebook_TG_json:
        phonebook_TG_json.write(json.dumps(phonebook, ensure_ascii=False)) 
    bot.send_message(message.chat.id, "Changes were saved.")

@bot.message_handler(commands=['phone'])
def learn_about_contact(message):
    contact_to_input = bot.send_message(message.chat.id, "Input name of the contact to learn his or her phone:")
    bot.register_next_step_handler(contact_to_input, find_phone)

def find_phone(message):
    contact_to_find = message.text 
    for i in range(len(phonebook)):
        if phonebook[i] == contact_to_find:
            bot.send_message(message.chat.id, f'Contact found: {phonebook[i]}, {phonebook[i+1]}')

@bot.message_handler(commands=['remove'])
def find_contact_to_remove(message):
    contact_to_remove_found = bot.send_message(message.chat.id, "Input name of the contact to remove him or her from your book:")
    bot.register_next_step_handler(contact_to_remove_found, remove_contact)

def remove_contact(message):
    contact_to_remove = message.text 
    for i in range(len(phonebook)):
        if phonebook[i] == contact_to_remove:
            phonebook.remove(phonebook[i+1])
            phonebook.remove(phonebook[i])
            break
    bot.send_message(message.chat.id, 'Contact was removed from your book!')

@bot.message_handler(commands=['editname'])
def find_contact_to_edit(message):
    contact_to_edit_found = bot.send_message(message.chat.id, "Input name of the contact to edit:")
    bot.register_next_step_handler(contact_to_edit_found, find_contact_position)

def find_contact_position(message):
    contact_to_edit = message.text
    for i in range(len(phonebook)):
        if phonebook[i] == contact_to_edit:
            new_name = bot.send_message(message.chat.id, f"Current name is {phonebook[i]}. Input new name:")
            break
    temp_data = {"old_name": phonebook[i], "new_name": None}
    bot.register_next_step_handler(new_name, give_new_name, temp_data)

def give_new_name(message, temp_data):
    temp_data["new_name"] = message.text
    new_name = temp_data["new_name"]
    old_name = temp_data["old_name"]
    for i in range(len(phonebook)):
        if phonebook[i] == old_name:
            phonebook[i] = new_name
            break
    bot.send_message(message.chat.id, f"Corrections were accepted. The contact's name is {new_name}.")

@bot.message_handler(commands=['editphone']) 
def find_contact_to_edit_phone(message):
    contact_to_edit_found = bot.send_message(message.chat.id, "Input name of the contact to edit:")
    bot.register_next_step_handler(contact_to_edit_found, find_contact_position_to_edit_phone)

def find_contact_position_to_edit_phone(message):
    contact_to_edit = message.text
    for i in range(len(phonebook)):
        if phonebook[i] == contact_to_edit:
            new_phone = bot.send_message(message.chat.id, f"Current phone is {phonebook[i+1]}. Input new phone:")
            break
    temp_data = {"old_phone": phonebook[i+1], "new_phone": None}
    bot.register_next_step_handler(new_phone, give_new_phone, temp_data)

def give_new_phone(message, temp_data):
    temp_data["new_phone"] = message.text
    new_phone = temp_data["new_phone"]
    old_phone = temp_data["old_phone"]
    for i in range(len(phonebook)):
        if phonebook[i] == old_phone:
            phonebook[i] = new_phone
            bot.send_message(message.chat.id, f"New phone number is {new_phone}")

bot.polling()