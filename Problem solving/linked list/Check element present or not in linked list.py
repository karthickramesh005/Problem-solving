# Check element present or not in linked list :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_key_present(head, key):
    current = head

    while current is not None:
        if current.data == key:
            return True
        current = current.next

    return False

# Example Usage
def create_linked_list(elements):
    if not elements:
        return None

    head = Node(elements[0])
    current = head

    for data in elements[1:]:
        current.next = Node(data)
        current = current.next

    return head

# Example
elements = [1, 2, 3, 4]
key_to_find = 3

# Create the linked list
head_of_linked_list = create_linked_list(elements)

# Check if the key is present
result = is_key_present(head_of_linked_list, key_to_find)

# Output
print(result)  # Output: True
