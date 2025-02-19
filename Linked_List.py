class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        
class Linked_list:
    def __init__(self,val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop(self):
        pre = self.head
        temp = self.head
        if self.length == 0:
            return None
        while(temp.next):
            pre = temp
            temp = pre.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
                
    def get(self,index):
        if index < 0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val
            
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.val = value
            return True
        return False 
        
    def print(self):
        temp = self.head
        while temp!= None:
            print(temp.val)
            temp = temp.next
            
