from collections import deque
from typing import Deque, List

class Graph:
    def __init__(self) -> None:
        self.n = int(input("Enter number of nodes: "))
        self.nodes = {i+1: [] for i in range(self.n)}
    
    def addEdge(self, start: int, end: int):
        self.nodes[start].append(end)
        self.nodes[end].append(start)
    
    def printGraph(self):
        for node, adj_list in self.nodes.items():
            print(f"{node} -> ", end="")
            for vertex in adj_list:
                print(vertex, end=" ")
            print()
    
    # Non-recursive DFS using stack with 'visited' message after each visit
    def dfs(self, start: int):
        visited = [False] * (self.n + 1)
        stack = [start]
        visited_nodes = []  # List to store visited nodes
        print(f"DFS from {start}: ")

        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                visited_nodes.append(current)  # Add visited node to the list
                print(f"{current} visited")
                # Add unvisited adjacent nodes to the stack
                for adjacentNode in reversed(self.nodes[current]):
                    if not visited[adjacentNode]:
                        stack.append(adjacentNode)
        
        # Print the list of all visited nodes at the end of DFS
        print(f"Visited nodes: {visited_nodes}")
        print("DFS traversal complete!\n")
    
    # BFS with 'visited' message after each visit
    def bfs(self, start: int):
        visited = [False] * (self.n + 1)
        queue = deque([start])
        visited[start] = True
        visited_nodes = []  # List to store visited nodes
        print(f"BFS from {start}: ")

        while queue:
            current = queue.popleft()
            visited_nodes.append(current)  # Add visited node to the list
            print(f"{current} visited")
            for adjacentNode in self.nodes[current]:
                if not visited[adjacentNode]:
                    queue.append(adjacentNode)
                    visited[adjacentNode] = True
        
        # Print the list of all visited nodes at the end of BFS
        print(f"Visited nodes: {visited_nodes}")
        print("BFS traversal complete!\n")

g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(5, 4)
g.printGraph()
g.dfs(3)
g.bfs(1)
