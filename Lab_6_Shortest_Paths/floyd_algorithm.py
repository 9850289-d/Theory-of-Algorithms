import heapq

INF = float("inf")

# Граф варіанту 9: вершини 1..8, ребра (u, v, вага)
V = 8
EDGES = [
    (1, 3, 6), (1, 4, 7), (1, 6, 8), (2, 4, 3), (2, 5, 4), (2, 6, 2),
    (3, 6, 3), (3, 8, 7), (4, 5, 9), (5, 7, 5), (6, 7, 9), (6, 8, 3),
]

def build_weight_matrix(n: int, edges: list) -> list:
    """Вагова матриця W: 0 на діагоналі, INF – ребра немає."""
    w = [[INF] * n for _ in range(n)]
    for i in range(n):
        w[i][i] = 0
    for u, v, weight in edges:
        w[u - 1][v - 1] = weight
        w[v - 1][u - 1] = weight
    return w


def floyd(w: list) -> list:
    """Алгоритм Флойда. Повертає матрицю найкоротших відстаней D."""
    n = len(w)
    d = [row[:] for row in w]               # D <- W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


# Виконання:
d = floyd(build_weight_matrix(V, EDGES))
print("    " + "".join(f"{j:>4}" for j in range(1, V + 1)))
for i, row in enumerate(d, start=1):
    print(f"{i:>3} " + "".join(f"{x:>4}" for x in row))
