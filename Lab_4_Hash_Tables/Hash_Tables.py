# ===== Лістинг 4.1 =====
import math

# Константи розмірів таблиць
M_DIV = 13   # метод ділення:   h(K) = K mod 13
M_MUL = 16   # метод множення:  h(K) = floor(16 * (K*A mod 1))
A = (math.sqrt(5) - 1) / 2   # константа Кнута, A ≈ 0.6180339887

# Вхідна послідовність (варіант 9)
PROVERB = "Чужу біду руками розведу, а до своєї розуму не дійду"
WORDS = [w.strip(",").upper() for w in PROVERB.split()]

# Номери позицій літер українського алфавіту (рис. 4.3 методичних вказівок)
ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
LETTER_POSITIONS = {ch: pos for pos, ch in enumerate(ALPHABET, start=1)}


def key_value(word: str) -> int:
    """Числовий ключ K = сума номерів позицій літер слова."""
    return sum(LETTER_POSITIONS.get(ch, 0) for ch in word)


def hash_div(k: int) -> int:
    """Метод ділення: h(K) = K mod 13."""
    return k % M_DIV


def hash_mul(k: int) -> int:
    """Метод множення: h(K) = floor(16 * (K*A mod 1))."""
    return math.floor(M_MUL * ((k * A) % 1))


def build_open_hash_table(words: list, m: int, hash_func) -> list:
    """Будує хеш-таблицю з роздільними ланцюжками (списками)."""
    # 1. Ініціалізація таблиці: m порожніх ланцюжків
    hash_table = [[] for _ in range(m)]

    # 2. Обробка кожного слова
    for word in words:
        address = hash_func(key_value(word))
        # Додавання слова в кінець відповідного ланцюжка
        hash_table[address].append(word)

    return hash_table


def display_hash_table(table: list, title: str):
    """Виводить відкриту хеш-таблицю у зручному форматі."""
    print(f"\n--- {title} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


# Виконання:
open_div = build_open_hash_table(WORDS, M_DIV, hash_div)
open_mul = build_open_hash_table(WORDS, M_MUL, hash_mul)
display_hash_table(open_div, "Ланцюжки, метод ділення (m=13)")
display_hash_table(open_mul, "Ланцюжки, метод множення (m=16)")


# ===== Лістинг 4.2 =====
def build_closed_hash_table(words: list, m: int, hash_func) -> list:
    """Будує хеш-таблицю з відкритою адресацією (лінійне дослідження)."""
    # 1. Ініціалізація таблиці: m порожніх комірок (None)
    hash_table = [None] * m

    # 2. Обробка кожного слова
    for word in words:
        start_address = hash_func(key_value(word))

        # Лінійне дослідження: h(k, i) = (h(k) + i) mod m
        for i in range(m):
            address = (start_address + i) % m
            # Комірка вільна – вставляємо ключ
            if hash_table[address] is None:
                hash_table[address] = word
                break
        else:
            # Цикл завершився без break – таблиця заповнена
            print(f"Помилка: таблиця заповнена, слово {word} не додано")

    return hash_table


def display_closed_table(table: list, title: str):
    """Виводить закриту хеш-таблицю у зручному форматі."""
    print(f"\n--- {title} ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


# Виконання:
closed_div = build_closed_hash_table(WORDS, M_DIV, hash_div)
closed_mul = build_closed_hash_table(WORDS, M_MUL, hash_mul)
display_closed_table(closed_div, "Відкрита адресація, метод ділення (m=13)")
display_closed_table(closed_mul, "Відкрита адресація, метод множення (m=16)")


# ===== Лістинг 4.3 =====
def search_chain(table: list, word: str, hash_func) -> int:
    """Кількість порівнянь при пошуку слова в ланцюжку T[h(k)]."""
    comparisons = 0
    for item in table[hash_func(key_value(word))]:
        comparisons += 1
        if item == word:
            break
    return comparisons


def search_closed(table: list, word: str, hash_func) -> int:
    """Кількість порівнянь при пошуку з лінійним дослідженням."""
    m = len(table)
    start = hash_func(key_value(word))
    comparisons = 0
    for i in range(m):
        comparisons += 1
        if table[(start + i) % m] == word:
            break
    return comparisons


tables = [
    ("Ланц. h1", open_div, search_chain, hash_div),
    ("Ланц. h2", open_mul, search_chain, hash_mul),
    ("Відкр. h1", closed_div, search_closed, hash_div),
    ("Відкр. h2", closed_mul, search_closed, hash_mul),
]
results = [{w: find(t, w, h) for w in WORDS} for _, t, find, h in tables]


def print_row(label, values, fmt="<9"):
    print(f"{label:<8} | " + " | ".join(f"{v:{fmt}}" for v in values))


print_row("Слово", [name for name, *_ in tables])
for word in WORDS:
    print_row(word, [r[word] for r in results])
print_row("Сума", [sum(r.values()) for r in results])
print_row("Середнє", [sum(r.values()) / len(r) for r in results], "<9.2f")
print_row("Максимум", [max(r.values()) for r in results])
for (name, *_), r in zip(tables, results):
    worst = [w for w, c in r.items() if c == max(r.values())]
    print(f"Максимум порівнянь ({name}): {', '.join(worst)}")
