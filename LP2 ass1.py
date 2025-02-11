#THIs is pactice code dont use it 

from collections import defaultdict, deque
import random

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph

    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = set()

        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            v = queue.popleft()
            print(v, end=' ')


            
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                


# Taking input from user
g = Graph()
num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))

print("Enter edges (u v) one by one:")

# Taking random or manual edges
for _ in range(num_edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

# Asking for start node
start_node = int(input("Enter the starting node for traversal: "))

print("\nDFS Recursive Traversal:")
g.dfs_recursive(start_node)

print("\n\nBFS Traversal:")
g.bfs(start_node)

