# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона, адрес - данные, которые должны находиться в файле. <----- 1
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

#1. Создать файл phonebook.txt 
#   -Обратимся к файлу phonebook.txt в режиме append ("a")  | ??

#2. Ввод данных (запись контакта) | +++++++++++++++++           
#   -Получить от пользователя данные по новому контакту | +++++++++++++++
#   -Подготовить данные к записи | +++++++++++++++++
#   -Обратимся к файлу phonebook.txt в режиме append ("a") | +++++++++++++++++
#   -Добавить полученные данные | +++++++++++++++++

#3. Вывод всех данных на экран | +++++++++++++++++
#   -Обратимся к файлу phonebook.txt в режиме read ("r") | +++++++++++++++++
#   -Вывести на экран все данные из файла | +++++++++++++++++

#4. Пользовательский поиск по характеристике 
#   -Выбрать вариант поиска (по имени, фамилии или телефону) | +++++++++++++++++
#   -Получить данные для поиска | +++++++
#   -Обратимся к файлу phonebook.txt в режиме read ("r") | +++++++++++++++++
#   -Осуществим поиск по файлу | +++++++++++++++++
#   -Выведем на экран (если найдем совпадение) | +++++++++++++++++

#5. Пользовательский интерфейс
#   Просто сделать | +++++++++++++++++

def file_read():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def file_append(text=""):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(text)

#Функции ввода
def input_sur():
    return input("Введите Фамилию: ")

def input_name():
    return input("Введите Имя: ")

def input_pat():
    return input("Введите Отчество: ")

def input_phone():
    return input("Введите Телефон: ")

def input_adr():
    return input("Введите Адрес: ")
#--Функции ввода

def input_data():
    sur = input_sur() 
    name = input_name()
    pat = input_pat()
    phone = input_phone()
    adr = input_adr()
    contact_str = f"{sur} {name} {pat} {phone}\n{adr}\n\n" #Форматирование для записи
    file_append(contact_str)

def print_data():
    print(file_read())

#Поиск
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
#--Поиск

#user menu (interface)
def u_interface():
    file_append() # - создание файла
    command = ""
    while command != "4":
        print("Меню:\n"
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n"
            "4. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1","2","3","4"):        
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
                print("Всего хорошего!")
        


if __name__ == "__main__":
    u_interface()
