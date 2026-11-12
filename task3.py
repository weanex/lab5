
from graph import Graph


def dfs_topological_sort(graph: Graph):

    visited = set()
    order = []          # порядок завершения 

    def dfs(v):
        visited.add(v)
        for (u, _w) in graph.neighbors(v):
            if u not in visited:
                dfs(u)
        order.append(v)   # добавляем после всех потомков

    for v in graph.vertices():
        if v not in visited:
            dfs(v)

    order.reverse()       # топологический порядок
    return order


def build_pancake_graph() -> Graph:
    g = Graph()
    edges = [
        ("3/4 cup milk",  "1 cup mix"),
        ("1 egg",         "1 cup mix"),
        ("1 Tb oil",      "1 cup mix"),
        ("1 cup mix",     "heat syrup"),
        ("1 cup mix",     "pour 1/4 cup"),
        ("heat griddle",  "pour 1/4 cup"),
        ("pour 1/4 cup",  "turn when bubbly"),
        ("turn when bubbly", "eat"),
        ("heat syrup",    "eat"),
    ]
    for u, v in edges:
        g.add_edge(u, v)
    return g


if __name__ == "__main__":
    g = build_pancake_graph()
    result = dfs_topological_sort(g)
    print("Топологический порядок шагов:")
    for i, step in enumerate(result, 1):
        print(f"{i}. {step}")