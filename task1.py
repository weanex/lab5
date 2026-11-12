
from collections import deque
from graph import Graph


def bfs(graph: Graph, start):
    visited = {start}
    distance = {start: 0}
    order = []
    queue = deque([start])

    while queue:
        v = queue.popleft()
        order.append(v)
        for (u, _w) in graph.neighbors(v):
            if u not in visited:
                visited.add(u)
                distance[u] = distance[v] + 1
                queue.append(u)

    return order, distance


if __name__ == "__main__":
    g = Graph()
    # пример графа из лекции
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("C", "D"),
        ("D", "E"),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    order, dist = bfs(g, "A")
    print("Порядок обхода BFS:", order)
    print("Расстояния:", dist)