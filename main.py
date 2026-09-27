class Node:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None     

if __name__ == "__main__":
    supplies = LinkedList()
    print(supplies.head)   # None — list is empty