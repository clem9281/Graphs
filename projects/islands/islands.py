# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

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

def get_island_neighbors(x, y, matrix):
    neighbors = []
    north = y - 1
    south = y + 1
    east = x - 1
    west = x + 1
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors

def dft_islands(start_x, start_y, matrix, visited):
    s = Stack()
    s.push((start_x, start_y))
    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_island_neighbors(x, y, matrix):
                s.push(neighbor)
    return visited    

def island_counter(matrix):
    visited = []
    counter = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[i]))
    # I think in the demo project the x and y were incorrectly swapped here, the y should be first
    for y in range(len(matrix)):
        for x in range(len(matrix[i])):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dft_islands(x,y,matrix,visited)
                    counter += 1
    return counter


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]



print(island_counter(islands)) # returns 4


big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(big_islands))