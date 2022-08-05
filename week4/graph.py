from collections import deque

undirectedGraph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'E', 'D'],
    'D': ['C', 'F'],
    'E': ['A', 'B', 'C', 'F'],
    'F': ['B', 'D', 'E'],
}

directedGraph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': ['E', 'D'],
    'D': [],
    'E': ['A'],
    'F': ['D', 'E']
}

# Find all of the nodes on a graph from the starting node.
# Breadth First Search
def bfs(graph, node):
    visited = [] # List to keep track of visited nodes.
    queue = deque() # Initialize a queue.
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited

print("Undirected Graph: ")
print(bfs(undirectedGraph, 'D'))

print("\nDirected Graph: ")
print(bfs(directedGraph, 'D'))