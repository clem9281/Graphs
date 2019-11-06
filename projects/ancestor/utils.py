import string

# Thought I would practice writing these from memory: a little different than we usually do
class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class Stack:
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
        return f"Stack: {arr}"
    
    def size(self): 
        return self.length
    
    def push(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def pop(self):
        old_node = self.head
        self.head = old_node.next
        self.length -= 1
        return old_node.value
    
    
# didn't end up needing the Queue
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
# letters = list(string.ascii_lowercase)
# q = Queue()
# for letter in letters:
#     q.enqueue(letter)
# print(q)
# print(q.size())
# q.dequeue()
# print(q)
# print(q.size())
# q.dequeue()
# print(q)
# print(q.size())
# q.dequeue()
# print(q)
# print(q.size())
# q.dequeue()
# print(q)
# print(q.size())
# letters = list(string.ascii_lowercase)
# s = Stack()
# for letter in letters:
#     s.push(letter)
# print(s)
# print(s.size())
# s.pop()
# print(s)
# print(s.size())
# s.pop()
# print(s)
# print(s.size())
# s.pop()
# print(s)
# print(s.size())
# s.pop()
# print(s)
# print(s.size())