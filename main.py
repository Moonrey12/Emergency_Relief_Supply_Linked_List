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

    def delete(self, name):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        current = self.head
        previous = None

        while current is not None:
            if current.name.lower() == name.lower():
                if previous is None:
                    self.head = current.next  # Deleting the head node
                else:
                    previous.next = current.next  # Skipping the current node
                print(f"{current.name} deleted.")
                return
            
            # Move pointers forward
            previous = current
            current = current.next

        print(f"{name} not found. Nothing deleted.")


def main():
    supplies = LinkedList()

    while True:
        print("\n========================================")
        print(" Emergency Relief Supply Management")
        print("========================================")
        print("1. Add Supply")
        print("2. Delete Supply")
        print("3. Search Supply")
        print("4. Display Supplies")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Supply name: ")
            quantity = int(input("Quantity: "))
            supplies.insert(name, quantity)
        elif choice == "2":
            name = input("Supply name to delete: ")
            supplies.delete(name)
        elif choice == "3":
            name = input("Supply name to search: ")
            supplies.search(name)
        elif choice == "4":
            supplies.display()
        elif choice == "5":
            print("Exiting program. Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()