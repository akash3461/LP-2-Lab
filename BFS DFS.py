from collections import defaultdict, deque
from typing import List

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since it's an undirected graph

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")

    # Non-recursive DFS using stack
    def dfs(self, start: int):
        visited = set()
        stack = [start]
        visited_nodes = []

        print(f"\nDFS from {start}:")

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                visited_nodes.append(current)
                print(f"{current} visited")
                # Add unvisited adjacent nodes to the stack (in reverse order for correct DFS order)
                for adjacent in reversed(self.graph[current]):
                    if adjacent not in visited:
                        stack.append(adjacent)
        
        print(f"Visited nodes: {visited_nodes}")
        print("DFS traversal complete!\n")

    # BFS using queue
    def bfs(self, start: int):
        visited = set()
        queue = deque([start])
        visited.add(start)
        visited_nodes = []

        print(f"\nBFS from {start}:")

        while queue:
            current = queue.popleft()
            visited_nodes.append(current)
            print(f"{current} visited")

            for adjacent in self.graph[current]:
                if adjacent not in visited:
                    queue.append(adjacent)
                    visited.add(adjacent)
        
        print(f"Visited nodes: {visited_nodes}")
        print("BFS traversal complete!\n")

# Taking input from user
g = Graph()
num_nodes = int(input("Enter the number of nodes: "))
num_edges = int(input("Enter the number of edges: "))

print("Enter edges (u v) one by one:")
for _ in range(num_edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

g.print_graph()

# Asking for start node
start_node = int(input("Enter the starting node for traversal: "))

print("\nDFS Traversal:")
g.dfs(start_node)

print("\nBFS Traversal:")
g.bfs(start_node)
