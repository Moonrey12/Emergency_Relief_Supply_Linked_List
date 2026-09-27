class Node:
    def __init__(self, name, quantity):
        self.name = name          # Store the supply name
        self.quantity = quantity  # Store the supply quantity
        self.next = None          # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None          # First node in the linked list

    def insert(self, name, quantity):
        new_node = Node(name, quantity)  # Create a new node

        if self.head is None:            # If the list is empty
            self.head = new_node         # Make the new node the head
            return

        current = self.head              # Start from the head
        while current.next is not None:  # Traverse to the last node
            current = current.next
        current.next = new_node          # Attach the new node at the end

    def display(self):
        if self.head is None:            # Check if list is empty
            print("No supplies available.")
            return

        current = self.head              # Start from the head
        print("Current Supplies:")
        while current is not None:       # Visit each node
            print(f"- {current.name}: {current.quantity}")
            current = current.next       # Move to the next node

    def search(self, name):
        current = self.head              # Start from the head
        while current is not None:       # Traverse the list
            if current.name.lower() == name.lower():  # Case-insensitive match
                print(f"{current.name} found! Quantity: {current.quantity}")
                return current            # Return the found node
            current = current.next        # Move to the next node
        print(f"{name} not found.")
        return None                       # Return None if not found

    def delete(self, name):
        if self.head is None:             # Check if list is empty
            print("List is empty. Nothing to delete.")
            return

        current = self.head               # Node to check
        previous = None                   # Previous node

        while current is not None:        # Traverse the list
            if current.name.lower() == name.lower():  # Match found
                if previous is None:      # Deleting the head node
                    self.head = current.next
                else:                     # Bypass the current node
                    previous.next = current.next
                print(f"{current.name} deleted.")
                return
            
            # Move pointers forward
            previous = current
            current = current.next

        print(f"{name} not found. Nothing deleted.")


def main():
    supplies = LinkedList()               # Create an empty supply list

    while True:                           # Menu loop
        print("\n========================================")
        print(" Emergency Relief Supply Management")
        print("========================================")
        print("1. Add Supply")
        print("2. Delete Supply")
        print("3. Search Supply")
        print("4. Display Supplies")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get user choice

        if choice == "1":                 # Add supply
            name = input("Supply name: ")
            quantity = int(input("Quantity: "))
            supplies.insert(name, quantity)
        elif choice == "2":               # Delete supply
            name = input("Supply name to delete: ")
            supplies.delete(name)
        elif choice == "3":               # Search supply
            name = input("Supply name to search: ")
            supplies.search(name)
        elif choice == "4":               # Display supplies
            supplies.display()
        elif choice == "5":               # Exit program
            print("Exiting program. Stay safe!")
            break
        else:                             # Invalid input
            print("Invalid choice. Please try again.")


if __name__ == "__main__":                # Run only if script is executed directly
    main()