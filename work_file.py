def choose_file(hint="Выберите файл из списка выше"):
    file_index = input(f"1 - phonebook\n2 - pb_copy\n{hint}: ")
    while file_index not in ("1", "2"):
        print("Некорректный ввод, повторите попытку")            
        file_index = input(f"1 - phonebook\n2 - pb_copy\n{hint}: ")
    if file_index == "1":
        return "phonebook.txt"
    else:
        return "pb_copy.txt"

def file_read(hint="Выберите файл из списка выше"):    
    with open(choose_file(hint), "r", encoding="UTF-8") as file:
        print()
        return file.read()
    


def file_append(text=""):
    with open(choose_file(), "a", encoding="UTF-8") as file:
        file.write(text)
    print()

def file_create(text=""):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(text)
    with open("pb_copy.txt", "a", encoding="UTF-8") as file:
        file.write(text)

def copy_append(text="",hint="Выберите куда скопировать данные: "): #Домашнее задание
    with open(choose_file(hint), "a", encoding="UTF-8") as file:
        file.write(text)
    print()
