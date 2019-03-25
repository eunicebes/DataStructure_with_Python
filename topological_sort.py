from collections import defaultdict

class graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.num_of_nodes = vertices

    def addEdge(self, u, v):
        ## the graph is directed
        self.graph[u].append(v)

    def dfs(self, root, visited, stack):
        visited.append(root)
        for neighbor in (self.graph[root]):
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)

        ## if this node finished, then push it into the stack
        stack.append(root)

    def topologicalSort(self):
        visited = []
        stack = []

        for i in range(self.num_of_nodes):
            if i not in visited:
                self.dfs(i, visited, stack)

        print(stack[::-1])

G = graph(6)
G.addEdge(5, 2)
G.addEdge(5, 0)
G.addEdge(4, 0)
G.addEdge(4, 1)
G.addEdge(2, 3)
G.addEdge(3, 1)
G.topologicalSort()