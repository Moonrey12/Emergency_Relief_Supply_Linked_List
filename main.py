class Node:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None     

    def insert(self, name, quantity):
        new_node = Node(name, quantity)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

if __name__ == "__main__":
    supplies = LinkedList()
    supplies.insert("Rice", 100)
    supplies.insert("Water", 200)
    supplies.insert("Blankets", 50)
    print(supplies.head.name, supplies.head.next.name, supplies.head.next.next.name)