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
                    temp.right = new_node 
                    return True
                temp = temp.right
            
    def contain(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:  # value == temp.value
                return True
        return False
    
    
    def BFS(self):
        curr_node = self.root
        result = []
        queue = []
        queue.append(curr_node)

        while len(queue)>0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return result

g = Binary_search_tree()
g.insert(47)
g.insert(21)
g.insert(76)
g.insert(18)
g.insert(27)
g.insert(52)
g.insert(82)
go = g.BFS()
print(go)