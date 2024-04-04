from csv import DictReader, DictWriter
from contact import Contact

class InvalidInputError(Exception):
    def __init__(self, txt):
        self.txt = txt

class FileHandler:
    @staticmethod
    def write_contacts(file_name, contacts):
        with open(file_name, "w", encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            for contact in contacts:
                f_writer.writerow({'Имя': contact.first_name, 'Фамилия': contact.last_name, 'Телефон': contact.phone_number})

    @staticmethod
    def read_contacts(file_name):
        contacts = []
        with open(file_name, "r", encoding='utf-8') as data:
            f_reader = DictReader(data)
            for row in f_reader:
                contacts.append(Contact(row['Имя'], row['Фамилия'], row['Телефон']))
        return contacts
    
    @staticmethod
    def export_contacts(file_name, contacts):
        with open(file_name, "w", encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            for contact in contacts:
                f_writer.writerow({'Имя': contact.first_name, 'Фамилия': contact.last_name, 'Телефон': contact.phone_number})

    @staticmethod
    def import_contacts(file_name):
        contacts = []
        with open(file_name, "r", encoding='utf-8') as data:
            f_reader = DictReader(data)
            for row in f_reader:
                contacts.append(Contact(row['Имя'], row['Фамилия'], row['Телефон']))
        return contacts
