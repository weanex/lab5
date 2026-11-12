
from graph import Graph


def transpose(graph: Graph) -> Graph:
    t = Graph()
    for v in graph.vertices():
        t.add_vertex(v)             
    for u in graph.vertices():
        for (v, w) in graph.neighbors(u):
            t.add_edge(v, u, w)      
    return t


if __name__ == "__main__":
    g = Graph()
    for u, v in [(0, 1), (0, 2), (2, 1), (1, 3)]:
        g.add_edge(u, v)

    print("Исходный граф:")
    print(g)
    print("\nОбращённый граф:")
    print(transpose(g))