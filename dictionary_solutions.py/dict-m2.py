def add_contact(address_book, name, phone=None, email=None, address=None):
    address_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
contact = {}
add_contact(contact, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contact, "Bob", phone="987-654-3210")
add_contact(contact, "Alice", address="123 Main St")

print(contact)
