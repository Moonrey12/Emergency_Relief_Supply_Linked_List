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


    def display(self):
        if self.head is None:
            print("No supplies available.")
            return

        current = self.head
        print("Current Supplies:")
        while current is not None:
            print(f"- {current.name}: {current.quantity}")
            current = current.next


    def search(self, name):
        current = self.head
        while current is not None:
            if current.name.lower() == name.lower():
                print(f"{current.name} found! Quantity: {current.quantity}")
                return current
            current = current.next
        print(f"{name} not found.")
        return None

if __name__ == "__main__":
    supplies = LinkedList()
    supplies.insert("Rice", 100)
    supplies.insert("Water", 200)
    supplies.insert("Blankets", 50)
    supplies.search("Water")
    supplies.search("Laptop")

    
    supplies.display()