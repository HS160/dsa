class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node  # Front of the queue
        self.last = new_node   # End of the queue
        self.length = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            print("Queue is empty")
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self.length -= 1
        return temp.value

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


# Example Usage
sc = Queue(4)
sc.enqueue(44)
sc.enqueue(45)
sc.enqueue(41)
sc.print_queue()

print("Dequeued:", sc.dequeue())
sc.print_queue()