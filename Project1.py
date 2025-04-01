import pickle
from dataclasses import dataclass, field
from typing import List


@dataclass
class Contact:
    name: str
    phone: str

    def __repr__(self) -> str:
        return f"{self.name} ({self.phone})"


class AddressBook:
    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def add_contact(self, name: str, phone: str) -> None:
        self.contacts.append(Contact(name, phone))
        print(f"Контакт {name} додано.")

    def list_contacts(self) -> None:
        if not self.contacts:
            print("Адресна книга порожня.")
            return
        print("\nСписок контактів:")
        for contact in self.contacts:
            print(f"- {contact}")


def save_data(book: AddressBook, filename: str = "address_book.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = "address_book.pkl") -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return AddressBook()


def main() -> None:
    book = load_data()

    while True:
        print("\nАдресна книга")
        print("1. Додати контакт")
        print("2. Переглянути контакти")
        print("3. Вийти")

        choice = input("Виберіть опцію (1/2/3): ").strip()

        if choice == '1':
            name = input("Введіть ім'я: ").strip()
            phone = input("Введіть номер телефону: ").strip()
            book.add_contact(name, phone)

        elif choice == '2':
            book.list_contacts()

        elif choice == '3':
            save_data(book)
            print("Дані збережено. Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
