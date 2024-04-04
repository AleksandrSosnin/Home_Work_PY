class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

    def find_contact_by_name(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.first_name.lower() or name.lower() in contact.last_name.lower():
                found_contacts.append(contact)
        return found_contacts
