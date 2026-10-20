# Лістинг 2.2 – Python-код рекурсивної реалізації алгоритму сортування злиттям.

def merge_sort_recursive_with_counters(arr):
    """
    Рекурсивне сортування злиттям (Divide and Conquer).
    Ділить масив навпіл доти, доки не залишаться масиви з 1 елемента,
    а потім "на зворотному шляху" зливає їх у відсортовані списки.
    """
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    
    # Базовий випадок: масив з 0 або 1 елемента вже відсортований
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
        
    mid = len(arr) // 2  # Знаходимо середину масиву
    assignments += 1
    
    # Рекурсивно сортуємо ліву та праву половини
    left_half, c1, a1, r1 = merge_sort_recursive_with_counters(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive_with_counters(arr[mid:])
    
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    
    # Зливаємо дві відсортовані половини разом
    merged_arr, c_merge, a_merge = merge_rec(left_half, right_half)
    comparisons += c_merge
    assignments += a_merge
    
    return merged_arr, comparisons, assignments, recursive_calls

def merge_rec(left, right):
    """
    Допоміжна функція злиття для рекурсивної версії.
    Приймає два відсортовані списки і повертає один новий відсортований список.
    """
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0  # Вказівник для лівого списку
    j = 0  # Вказівник для правого списку
    
    # Порівнюємо поточні елементи обох списків і додаємо менший до результату
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
        
    # Якщо в лівому списку залишилися елементи, додаємо їх в кінець
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1
        
    # Якщо в правому списку залишилися елементи, додаємо їх в кінець
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1
        
    return merged_arr, comparisons, assignments

# === Блок тестування ===
my_list = [12, 23, 67, 65, 50, 70, 80, 61, 92]
print("Оригінальний список:", my_list)

# Запускаємо рекурсивне сортування
sorted_list, total_comps, total_assigs, total_calls = merge_sort_recursive_with_counters(my_list)

print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {total_comps}")
print(f"Загальна кількість присвоювань: {total_assigs}")
print(f"Загальна кількість рекурсивних викликів: {total_calls}")
