import string
# in class exercise

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


f = open('short-words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

print(word_set)
def get_neighbors(word):
    letters = list(string.ascii_lowercase)
    neighbors = []
    letter_list = list(word)
    for i in range(len(letter_list)):
        for letter in letters:
            temp_word = list(letter_list)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

def ladder(starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            print(q.queue)
            path = q.dequeue()
            v = path[-1]
            print(v)
            if v not in visited:
                    if v == destination_vertex:
                        return path
                    visited.add(v)
                    for neighbor in get_neighbors(v):
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        q.enqueue(path_copy)
        return None

print(get_neighbors('hit'))
print(ladder('hit', 'cog'))