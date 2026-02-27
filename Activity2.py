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

contacts = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
print(search_contact(contacts, "Eve"))