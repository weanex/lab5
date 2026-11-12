
import heapq
from graph import Graph


def dijkstra(graph: Graph, start, end):

    # расстояния
    dist = {v: float("inf") for v in graph.vertices()}
    dist[start] = 0
    # предки для восстановления пути
    prev = {v: None for v in graph.vertices()}
    # приоритетная очередь (стоимость, вершина)
    pq = [(0, start)]
    visited = set()

    while pq:
        d, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        if v == end:
            break
        for (u, w) in graph.neighbors(v):
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                prev[u] = v
                heapq.heappush(pq, (nd, u))

    if dist[end] == float("inf"):
        return None, None

    # восстановление пути
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path, dist[end]


def build_variant2_graph() -> Graph:
    g = Graph()
    edges = [
        ("Белово",              "Ленинск-Кузнецкий", 25),
        ("Белово",              "Гурьевск",          40),
        ("Ленинск-Кузнецкий",   "Гурьевск",          60),
        ("Ленинск-Кузнецкий",   "Мыски",             180),
        ("Ленинск-Кузнецкий",   "Кемерово",          90),
        ("Ленинск-Кузнецкий",   "Новосибирск",       250),
        ("Киселевск",           "Ленинск-Кузнецкий", 30),
        ("Киселевск",           "Новосибирск",       280),
        ("Гурьевск",            "Мыски",             150),
        ("Мыски",               "Кемерово",          220),
        ("Новосибирск",         "Кемерово",          250),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g


if __name__ == "__main__":
    g = build_variant2_graph()
    print("вариант 2 ")
    print(g)

    while True:
        print("\n Поиск кратчайшего пути ")
        a = input("Город А (или 'q' для выхода): ").strip()
        if a.lower() == "q":
            break
        b = input("Город Б: ").strip()

        path, dist = dijkstra(g, a, b)
        if path is None:
            print(f"Пути из «{a}» в «{b}» нет.")
        else:
            print(f"Минимальный путь: {' -> '.join(path)}")
            print(f"Количество километров: {dist} км")