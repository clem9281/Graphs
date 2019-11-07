class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        node = self.head
        arr = [None] * self.length
        counter = 0
        while node:
            arr[counter] = node.value
            node = node.next
            counter += 1
        return f"Queue: {arr}"
    
    def size(self): 
        return self.length
    
    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def dequeue(self):
        old_node = self.head
        self.head = old_node.next
        self.length -= 1
        return old_node.value