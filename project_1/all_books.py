
import add_books
import view_all_books
import remove_books
import search_books

all_books = []

while True:
    print("Welcome to Contact Book Management System")
    
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

    menu = input("Select any number : ")

    if menu == "1":
        all_books = add_books.add_books(all_books)
    
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    
    elif menu == "3":
        remove_books.remove_books(all_books)

    elif menu == "4":
        search_books.search_books(all_books)

    elif menu == "5":
        print("Thanks for using Contact Book Management System")
        break

    else:
        print("Sorry.")





