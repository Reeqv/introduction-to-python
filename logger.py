from data_create import *
from work_file import *

def print_data():
    print(file_read())

def input_data():
    sur = input_sur() 
    name = input_name()
    pat = input_pat()
    phone = input_phone()
    adr = input_adr()
    contact_str = f"{sur} {name} {pat} {phone}\n{adr}\n\n" #Форматирование для записи
    file_append(contact_str)

def search_contact():
    print("Возможные варианты поиска:\n"
         "1. По фамилии\n"
         "2. По имени\n"
         "3. По отчеству\n"
         "4. По номеру телефона\n"
         "5. По адресу\n")    
    command = input("Выберите вариант поиска: ")

    while command not in ("1","2","3","4","5"):        
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска: ")
    
    i_var = int(command) - 1

    search = input("Введите данные для поиска: ")
    print()
    contacts_list = file_read().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        cont_list = contact_str.replace("\n"," ").split()
        if search in cont_list[i_var]:
            print(contact_str)
            print()

def copy_contact(): #Домашнее задание

    list_split = file_read(hint="Выберите источник для копирования").rstrip().split("\n\n")
    print(list_split)
    for i in range(len(list_split)):
        print(f"[{i+1}] {list_split[i]}", end="\n\n")

    index_ = int(input("Выберите порядковый номер контакта: "))
    while index_ not in range(1,len(list_split)+1):
        print("Некорректный ввод, повторите попытку")
        index_ = int(input("Выберите порядковый номер контакта: "))
    print("")
    copy_append(str(list_split[index_-1]+"\n\n"))
    print("\nГотово!\n")