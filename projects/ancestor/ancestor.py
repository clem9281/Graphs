from utils import Stack
    
def earliest_ancestor(ancestors, starting_node):
    # we've got to load our ancestors into something we can work with quickly, otherwise we'll have to go back and forth over that array like a gajillion times to find each ancestor. We'll load it into a dict that has basically the same structure as that graph we've been working on
    family = {}
    for pair in ancestors:
        # also load everything in backwards, we only care about the ancestor direction not the decendant direction, so have decendants point to ancestors
        if not pair[1] in family:
            value = set()
            value.add(pair[0])
            family[pair[1]] = value
        else:
            family[pair[1]].add(pair[0])
    # Now that we have our relationships set up, we can look to see if the node we want to look at even has ancestors. If it is not a key in our dictionary it has no ancestors, return -1
    if starting_node not in family:
        return -1
    # We'll make up a dictionary that stores the distance of each element from our source, using dft to get the longest routes rather than the shortest ones
    dist = {starting_node: 0}
    s = Stack()
    s.push(starting_node)
    # we might have multiple nodes that are the same distance away, store the ones with the farthest distance, and then we'll get the one with the lowest numerical id
    farthest_nodes = set()
    farthest_distance = 0
    while s.size() > 0:
        current = s.pop()
        # if the node has ancestors, iterate over it's ancestors
        if current in family:
            for neighbor in family[current]:
                current_distance = dist[current] + 1
                # load each ancestor into our dictionary with it's distance from source
                dist[neighbor] = current_distance
                # if that distance farther than our current farthest, make this distance our new farthest distance and replace our farthest nodes with a new list containing the node we just found
                if current_distance > farthest_distance:
                    farthest_distance = current_distance
                    farthest_nodes = set()
                    farthest_nodes.add(neighbor)
                # if that distance is equal to our current farthest then add this node to our list of farthest nodes
                elif current_distance == farthest_distance:
                    farthest_nodes.add(neighbor)
                s.push(neighbor)
    # return the farthest node with the lowest value
    return min(farthest_nodes)

# this gives us all the paths from the source, it works I just liked my distance dictionary better
# def get_paths_from_source(source, family):
#         s = Stack()
#         s.push([source])
#         paths = []
#         while s.size() > 0:
#             path = s.pop()
#             v = path[-1]
#             if v in family:
#                 for neighbor in family[v]:
#                     path_copy = path.copy()
#                     path_copy.append(neighbor)
#                     s.push(path_copy)
#                     if neighbor not in family:
#                         paths.append(path_copy)
#         return paths
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 8))
# print(earliest_ancestor(test_ancestors, 9))
# print(earliest_ancestor(test_ancestors, 10))
# print(earliest_ancestor(test_ancestors, 11))