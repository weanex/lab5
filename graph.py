class Graph:
    def __init__(self):
        
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))

    def vertices(self):
        return list(self.adj.keys())

    def neighbors(self, v):
        return self.adj.get(v, [])

    def __str__(self):
        lines = []
        for v in self.adj:
            lines.append(f"{v}: {self.adj[v]}")
        return "\n".join(lines)