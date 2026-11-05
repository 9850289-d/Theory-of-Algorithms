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


def find_set(parent: list, i: int) -> int:
    """FIND: представник множини, якій належить вершина i."""
    if i == parent[i]:
        return i
    # Рекурсивний пошук кореня
    return find_set(parent, parent[i])


def union_set(parent: list, u: int, v: int):
    """UNION: об'єднує множини з представниками u та v."""
    parent[u] = v


def kruskal(n: int, edges: list) -> list:
    """Алгоритм Крускала. Повертає ребра МКД (u, v, вага) у порядку вибору."""
    # Ініціалізація DSU: спочатку кожна вершина є власної батьківською вершиною
    parent = list(range(n))
    
    mst = []  # Список ребер для МКД
    
    # Крок 1: Сортуємо ребра за зростанням ваги (key=lambda e: e[2])
    sorted_edges = sorted(edges, key=lambda e: e[2])
    
    # Крок 2: Перебір сортованих ребер
    for u, v, w in sorted_edges:
        # Знаходимо кореневих представників для обох вершин ребра (переходимо до 0-індексації)
        u_rep = find_set(parent, u - 1)
        v_rep = find_set(parent, v - 1)
        
        # Якщо вершини належать до різних множин — ребро НЕ утворює цикл
        if u_rep != v_rep:
            mst.append((u, v, w))               # Додаємо ребро до МКД
            union_set(parent, u_rep, v_rep)     # Об'єднуємо множини
            
            # Якщо вже знайшли n - 1 ребер — МКД повністю сформовано
            if len(mst) == n - 1:
                break
                
    return mst


# === Основний блок виконання програми ===
if __name__ == "__main__":
    print("=== Алгоритм Крускала (Варіант 9) ===")
    
    # Виконуємо алгоритм Крускала
    mst_kruskal = kruskal(V, EDGES)
    
    # Виводимо результати
    for u, v, w in mst_kruskal:
        print(f"{u} - {v} : {w}")
        
    total_cost = sum(w for _, _, w in mst_kruskal)
    print(f"\nЗагальна вартість МКД: {total_cost}")
