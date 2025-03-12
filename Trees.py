class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        
class Binary_search_tree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        
        if self.root == None:
            self.root = new_node
        
        temp = self.root
        
        while(True):
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    return True
                temp = temp.right
            
    def contain(self,value):
        if self.root is None:
            return False
        temp = self.root
        if temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False