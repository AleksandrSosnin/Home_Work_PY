from phonebook import PhoneBook
from file_handler import FileHandler, InvalidInputError
from contact import Contact

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise InvalidInputError("Не валидное имя")
            else:
                is_valid_first_name = True
        except InvalidInputError as err:
            print(err)
            continue

    last_name = "Иванов"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise InvalidInputError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except InvalidInputError as err:
            print(err)
            continue

    return first_name, last_name, phone_number

def main():
    phone_book = PhoneBook()
    file_name = 'phone.csv'
    file_handler = FileHandler()

    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            contact_info = get_info()
            phone_book.add_contact(Contact(*contact_info))  # Распаковываем кортеж и передаем его как аргументы
        elif command == 'r':
            phone_book.display_contacts()
        elif command == 'e':
            file_handler.export_contacts(file_name, phone_book.contacts)
            print("Контакты успешно экспортированы в файл.")
        elif command == 'i':
            phone_book.contacts = file_handler.import_contacts(file_name)
            print("Контакты успешно импортированы из файла.")
        elif command == 'f':
            name = input("Введите имя или фамилию для поиска: ")
            found_contacts = phone_book.find_contact_by_name(name)
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
            else:
                print("Контакт не найден.")

if __name__ == "__main__":
    main()
