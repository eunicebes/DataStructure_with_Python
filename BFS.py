from collections import defaultdict

class graph:
    def __init__(self, num, is_undirected = True):
        self.graph = defaultdict(set)
        self.is_undirected = is_undirected

    def addEdge(self, u, v):
        self.graph[u].add(v)
        if self.is_undirected:
            self.graph[v].add(u)

    def BFS(self, start):
        visited = []
        queue = []

        queue.append(start)
        visited.append(start)

        while queue:
            node = queue.pop(0)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        print(visited)

G = graph(4)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.BFS(1)