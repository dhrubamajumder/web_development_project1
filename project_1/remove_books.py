#----------------------------------------------------------

from save_all_books import save_all_books

def remove_books(contact):
    numbers = input("\nEnter the phone number of the contact to remove: ").strip()
    for contacts in contact:
        if contacts['number'] == numbers:
            contact.remove(contacts)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")




