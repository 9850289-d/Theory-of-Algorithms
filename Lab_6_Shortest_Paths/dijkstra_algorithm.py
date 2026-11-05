import heapq

INF = float("inf")

# Граф варіанту 9: вершини 1..8, ребра (u, v, вага)
V = 8
EDGES = [
    (1, 3, 6), (1, 4, 7), (1, 6, 8), (2, 4, 3), (2, 5, 4), (2, 6, 2),
    (3, 6, 3), (3, 8, 7), (4, 5, 9), (5, 7, 5), (6, 7, 9), (6, 8, 3),
]


def build_adjacency_lists(n: int, edges: list) -> dict:
    """Списки суміжності: для кожної вершини пари (сусід, вага)."""
    adj = {v: [] for v in range(1, n + 1)}
    for u, v, w in sorted(edges):
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def dijkstra(adj: dict, s: int):
    """Алгоритм Дейкстри. Повертає (pred, dist) для стартової вершини s."""
    pred = {v: -1 for v in adj}             # попередники вершин
    dist = {v: INF for v in adj}            # довжини найкоротших шляхів
    dist[s] = 0
    pq = [(0, s)]                           # черга з пріоритетом
    while pq:
        d, u = heapq.heappop(pq)            # ExtractMinFromPQ
        if d > dist[u]:                     # застарілий запис черги
            continue
        for v, w in adj[u]:                 # перебір суміжних вершин
            if dist[v] > dist[u] + w:       # умова релаксації ребра
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))   # UpdatePQ
    return pred, dist


def get_path(pred: dict, v: int) -> list:
    """Відновлення шляху від стартової вершини до v за масивом pred."""
    path = []
    while v != -1:
        path.append(v)
        v = pred[v]
    return path[::-1]


# Виконання:
adj = build_adjacency_lists(V, EDGES)
s = 1
pred, dist = dijkstra(adj, s)
print("dist:", list(dist.values()))
print("pred:", list(pred.values()))
print(f"З вершини {s}:")
print("В вершину | Шлях | Вага")
for v in range(1, V + 1):
    if v != s:
        print(f"{v} | {' -> '.join(map(str, get_path(pred, v)))} | {dist[v]}")
