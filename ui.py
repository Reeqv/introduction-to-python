from logger import *

def u_interface():
    file_create() # - создание файла
    command = ""
    while command != "5":
        print("Меню:\n"
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n"
            "4. Скопировать контакт\n"
            "5. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1","2","3","4","5",):        
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню: ")

        print()        
        match command:            
            case "1":
                input_data()
            case "2":
                search_contact()
            case "3":
                print_data()
            case "4":
                copy_contact()
            case "5":
                print("Всего хорошего!")                