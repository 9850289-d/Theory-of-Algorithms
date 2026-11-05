# Нескінченність для позначення відсутності ребра між вершинами
INF = float("inf")

# Кількість вершин у графі (вершини 1..8)
V = 8

# Список ребер графа: (u, v, weight)
EDGES = [
    (1, 3, 6), (1, 4, 7), (1, 6, 8),
    (2, 4, 3), (2, 5, 4), (2, 6, 2),
    (3, 6, 3), (3, 8, 7),
    (4, 5, 9),
    (5, 7, 5),
    (6, 7, 9), (6, 8, 3),
]


def build_adjacency_matrix(n: int, edges: list) -> list:
"""Матриця суміжності (вагових коефіцієнтів); INF – ребра немає."""
    # Ініціалізуємо матрицю розміром n x n значеннями INF (нескінченність)
    matrix = [[INF] * n for _ in range(n)]
    
    # Оскільки ребра вхідного графа задані в 1-індексації (1..8),
    # приводимо їх до 0-індексації Python ([u-1][v-1])
    for u, v, w in edges:
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w  # Граф неорієнтований, тому матриця симетрична
        
    return matrix


def build_adjacency_lists(n: int, edges: list) -> list:
 """Списки суміжності: для кожної вершини пари (сусід, вага)."""
    lists = [[] for _ in range(n)]
    
    # Для впорядкованого виводу сортуємо ребра перед побудовою
    for u, v, w in sorted(edges):
        lists[u - 1].append((v, w))
        lists[v - 1].append((u, w))
        
    return lists


def prim(matrix: list, start: int = 0) -> list:  
"""Алгоритм Прима. Повертає ребра МКД (u, v, вага) у порядку вибору."""
 n = len(matrix)
    
    # Масив прапорців: True — вершина вже входить до МКД, False — ні
    selected = [False] * n
    selected[start] = True  # Включаємо початкову вершину
    
    mst = []  # Список ребер, що увійдуть до МКД
    
    # МКД для графа з n вершин завжди містить точно n - 1 ребер
    while len(mst) < n - 1:
        min_weight = INF
        x = -1  # Вершина у складі МКД
        y = -1  # Вершина поза складом МКД
        
        # Перебираємо всі вершини, які вже додані до МКД
        for i in range(n):
            if selected[i]:
                # Шукаємо найлегше ребро до вершин, які ще НЕ в МКД
                for j in range(n):
                    if not selected[j] and matrix[i][j] < min_weight:
                        min_weight = matrix[i][j]
                        x = i
                        y = j
                        
        # Якщо не знайшли жодного ребра, а МКД ще не побудовано — граф незв'язний
        if y == -1:
            break
            
        # Додаємо знайдене ребро до МКД (повертаємо 1-індексацію для виводу)
        mst.append((x + 1, y + 1, min_weight))
        
        # Позначаємо вершину y як включену до МКД
        selected[y] = True
        
    return mst


# === Основний блок виконання програми ===
if __name__ == "__main__":
    print("=== Алгоритм Прима (Варіант 9) ===")
    
    # 1. Будуємо матрицю суміжності
    adj_matrix = build_adjacency_matrix(V, EDGES)
    
    # 2. Виконуємо алгоритм Прима
    mst_prim = prim(adj_matrix, start=0)
    
    # 3. Виводимо результати
    for u, v, w in mst_prim:
        print(f"{u} - {v} : {w}")
        
    total_cost = sum(w for _, _, w in mst_prim)
    print(f"\nЗагальна вартість МКД: {total_cost}")
