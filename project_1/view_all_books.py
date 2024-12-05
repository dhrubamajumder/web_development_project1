

def view_all_books(all_books):
    if all_books !=[]:
        for book in all_books:
            print(f"name: {book['name']}| email: {book['email']}| number : {book['number']}| address {book['address']}\n")
    
    else:
        print("No Book Found in All Books")
