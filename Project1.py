import pickle

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def list_contacts(self):
        return self.contacts


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    while True:
        print("\nАдресна книга")
        print("1. Додати контакт")
        print("2. Переглянути контакти")
        print("3. Вийти")

        choice = input("Виберіть опцію (1/2/3): ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            book.add_contact(name, phone)
            print(f"Контакт {name} додано.")
        
        elif choice == '2':
            print("\nСписок контактів:")
            for contact in book.list_contacts():
                print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")
        
        elif choice == '3':
            save_data(book)
            print("Дані збережено. Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":