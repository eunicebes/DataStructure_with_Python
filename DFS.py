from collections import defaultdict

class graph:
    def __init__(self, vertices, is_undirected=True):
        self.graph = defaultdict(set)
        self.num_of_nodes = vertices
        self.is_undirected = is_undirected

    def addEdge(self, u, v):
        self.graph[u].add(v)
        if self.is_undirected:
            self.graph[v].add(u)

    ## execute DFS using recursive method
    def DFS(self, root, visited = None):
        if visited == None:
            visited = []

        visited.append(root)
        for neighbor in (self.graph[root]):
            if neighbor not in visited:
                self.DFS(neighbor, visited)
        return visited


G = graph(5)
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(3, 4)
print(G.DFS(0))

