def find_student(register, name):
    for student in register:
        if student == name:
            return "Student Found"
    return "Student Not Found"

students = ["Alice", "Bob", "Charlie", "David"]
print(find_student(students, "Charlie"))

def check_product(products, item):
    for product in products:
        if product == item:
            return "Product Available"
    return "Product Not Available"

store_items = ["Milk", "Eggs", "Bread", "Butter"]
print(check_product(store_items, "Eggs"))

def search_contact(contacts, name):
    left = 0
    right = len(contacts) - 1

    while left <= right:
        mid = (left + right) // 2

        if contacts[mid] == name:
            return "Contact Found"
        
        elif contacts[mid] < name:
            left = mid + 1

        else:
            right = mid - 1

    return "Contact Not Found"