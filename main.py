class Node:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.next = None

if __name__ == "__main__":
    test_node = Node("Rice", 100)
    print(test_node.name)
    print(test_node.quantity)
    print(test_node.next)        