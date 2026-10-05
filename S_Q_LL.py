class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
head = None
temp = None

for i in range(3):
    data = int(input("Enter value: "))
    newNode = Node(data)

    if head is None:
        head = newNode
        temp = newNode
    else:
        temp.next = newNode
        temp = newNode


# Display Stack
print("\nStack:")
temp = head

for i in range(3):
    print(temp.data, end=" ")
    temp = temp.next


# Display Queue
print("\n\nQueue:")
temp = head

for i in range(3):
    print(temp.data, end=" ")
    temp = temp.next