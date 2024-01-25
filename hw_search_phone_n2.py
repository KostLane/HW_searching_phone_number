def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            
        elif choice ==7:
            
            write_txt('phonebook.txt',phone_book)


        choice=show_menu()




def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменение номера телефона\n"
          "4. Удаление абонента из справочника\n"
          "5. Поиск по номеру телефона\n"
          "6. Добавление абонента в справочник\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Выйти из программы")
    choice = int(input())
    return choice


def read_txt(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        phone_book = file.readlines()
    return phone_book


def print_result(phone_book):
    for line in phone_book:
        print(line.strip())

def find_by_lastname(phone_book, last_name):
    for line in phone_book:
        if last_name in line:
            return line
    return "Абонент не найден"

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if last_name in phone_book[i]:
            phone_book[i] = phone_book[i].replace(last_name, new_number)
            return "Номер успешно изменен"
    return "Абонент не найден"

def delete_by_lastname(phone_book, lastname):
    for i in range(len(phone_book)):
        if lastname in phone_book[i]:
            del phone_book[i]
            return "Абонент успешно удален"
    return "Абонент не найден"

def find_by_number(phone_book, number):
    for line in phone_book:
        if number in line:
            return line
    return "Абонент не найден"

def add_user(phone_book, user_data):
    phone_book.append(user_data)
    return "Абонент успешно добавлен"

def write_txt(filename, phone_book):
    with open(filename, 'w',encoding='utf-8') as file:
        for line in phone_book:
            file.write(line + '\n')
    return "Телефонная книга успешно сохранена"



work_with_phonebook()