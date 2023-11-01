#Вывести список контактов с нумерацией
#Пользовательский ввод индекса контакта
#добавить контакт с нужным индексом в доп файл

from work_file import file_read
from work_file import copy_append
from ui import u_interface

def print_data_split():
    list_split = file_read().rstrip().split("\n\n")
    
    for i in range(len(list_split)):
        print(f"[{i+1}] {list_split[i]}", end="\n\n")
    print(len(list_split))

    index_ = int(input("Выберите порядковый номер контакта: "))
    while index_ not in range(1,len(list_split)+1):
        print("Некорректный ввод, повторите попытку")
        index_ = int(input("Выберите порядковый номер контакта: "))

    copy_append(list_split[index_-1])

print_data_split()
# if __name__ == "__main__":
#     u_interface()
