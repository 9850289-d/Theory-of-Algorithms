# Лістинг 2.1 – Python-код ітеративної реалізації алгоритму сортування злиттям.

def merge_sort_iterative(a):
    """
    Ітеративне сортування злиттям.
    Сортує масив, поступово об'єднуючи сусідні блоки розміром 1, 2, 4, 8 і т.д.,
    поки розмір блоку не перевищить довжину масиву.
    """
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1  # Початковий розмір підмасивів для злиття (починаємо з 1 елемента)
    
    while i < n:
        j = 0  # Індекс початку лівого підмасиву
        while j < n - i:
            left = j
            mid = j + i
            # Визначаємо кінець правого підмасиву (min гарантує, що ми не вийдемо за межі масиву)
            right = min(j + 2 * i, n)

            # Викликаємо функцію злиття для двох знайдених підмасивів
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            
            j += 2 * i  # Переходимо до наступної пари підмасивів
        i *= 2  # Подвоюємо розмір підмасивів для наступного проходу
        
    return a, comparisons, assignments

def merge(a, left, mid, right):
    """
    Допоміжна функція злиття двох відсортованих підмасивів (a[left:mid] та a[mid:right])
    в один відсортований сегмент безпосередньо в оригінальному масиві 'a'.
    """
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    
    # Створюємо тимчасові копії лівого (L) та правого (R) підмасивів
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    
    it1 = 0  # Вказівник для лівого підмасиву
    it2 = 0  # Вказівник для правого підмасиву
    k = left # Вказівник для оригінального масиву 'a' де ми будемо перезаписувати дані
    assignments += 3
    
    # Порівнюємо елементи з L та R і записуємо менший в масив 'a'
    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 2
        k += 1
        assignments += 1
        
    # Якщо в лівому підмасиві залишилися елементи, просто дописуємо їх
    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 1
        
    # Якщо в правому підмасиві залишилися елементи, дописуємо їх
    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 1
        
    return comparisons, assignments

# === Блок тестування ===
my_list = [12, 23, 67, 65, 50, 70, 80, 61, 92]
print("Оригінальний список:", my_list)
# Передаємо копію масиву, щоб не змінити оригінал
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоювань: {assigs}")
