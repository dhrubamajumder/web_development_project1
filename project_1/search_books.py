
def search_books(contancts):
    name = input("Enter the name to search : ").strip()
    # if name in contancts:
    #     info = contancts[name]
    #     print(f"\nName: {name}, Number: {info['number']}, Email: {info['email']}")
    # else:
    #     print("Contact not found. ")
    query_lower = str(name).lower()
    # Find matching dictionaries where query matches name or number
    results = [
        entry for entry in contancts
        if query_lower in entry['name'].lower() or query_lower in str(entry['number']).lower()
    ]
    print(results)