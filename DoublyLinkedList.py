class Node:
    def __init__(self, data):
        self.data = data        # Node value
        self.prev = None        # Pointer to previous node
        self.next = None        # Pointer to next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # First node in the list
        self.tail = None        # Last node in the list

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # List is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link new node after tail
            new_node.prev = self.tail
            self.tail = new_node       # Update tail

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                # If not the first node
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # It's the head

                # If not the last node
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # It's the tail

                return  # Exit after deleting
            current = current.next

    def display_forward(self):
        current = self.head
        print("Forward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        print("Backward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
