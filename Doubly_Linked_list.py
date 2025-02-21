class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Creating functions    

    def append(self,value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        self.length += 1
    
# Deleting functions
    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def pop_first(self):
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        
    
# Additional functions
    def get(self,index):
        if index<0 or index>self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp       
    
    def set_value(self,index,val):
        value = self.get(index)
        value.val = val

    def insert(self,index,val):
        new_node = Node(val)
        temp = self.get(index-1)
        after = temp.next
        temp.next = new_node
        new_node.next = after
        after.prev = new_node
        new_node.prev = temp
        self.length += 1

    def remove(self,index):
        temp = self.get(index-1)
        after = temp.next.next
        temp.next = after
        after.prev = temp
        self.length -= 1
        
# Printing functions
    
    def print(self):
        temp = self.head
        while temp!= None:
            print(temp.val)
            temp = temp.next
    
myDLL = Doubly_Linked_List(1)
myDLL.append(2)
myDLL.prepend(0)
searchfile = myDLL.get(2)
print(searchfile.val)
myDLL.set_value(index=2,val=50)
myDLL.insert(index=1,val=69)
myDLL.remove(index=2)
myDLL.print()