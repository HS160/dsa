class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class stack:
    def __init__(self,val):
        new_node = Node(val)
        self.bottom = new_node
        self.top = new_node
        self.height = 1
    
    def push(self,value):
        new_node = Node(value)
        self.top.next = new_node
        new_node.prev = self.top
        self.top = new_node
        self.height += 1
        
    def pop(self):
         self.top = self.top.prev
         self.top.next = None
         self.height-= 1
    
    def print(self):
        temp = self.top
        while temp!= None:
            print(temp.value)
            temp = temp.prev
s= stack(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print()