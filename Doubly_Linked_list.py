class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1