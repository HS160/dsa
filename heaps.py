from sys import last_value


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self,index):
        return 2*index + 1
    
    def right_child(self,index):
        return 2*index + 2
    
    def _parent(self, index):
        return (index-1)//2
    
    def swap(self, i1, i2):
        self.heap[i1],self.heap[i2] = self.heap[i2],self.heap[i1]
        
    def insert(self,val):
        self.heap.append(val)
        curr = len(self.heap)-1
        
        while curr > 0 and self.heap[curr]> self.heap[self._parent(curr)]:
            self.swap(curr,self._parent(curr))
            curr = self._parent(curr)
            
    
    def _sink_down(self,index):
        max_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)
            
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index            

            if max_index != index:
                self.swap(index,max_index)
                index = max_index
            else:
                return
            
    def remove(self):
        if len(self.heap) ==0:
            return None
        if len(self.heap) ==0:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0) 
        return max_value