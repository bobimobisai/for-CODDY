lst1 = [1, 34, 5, 23, 9, 12]
lst2 = [3, 534, 112, 9, 8, 2]


def get_sort(*lst: list) -> list:
    """
    Вернет отсортированный по убыванию список без дубликатов
    """
    if not all(isinstance(item, int) for sublist in lst for item in sublist):
        # выкидываем исключение если список не содержит чисел
        raise ValueError("Списки должны содержать только int")
    else:
        # складываем ВСЕ списки
        our_lst = sum(lst, [])
        # проверяем на дубликаты и убираем дубликаты
        no_dupl = list(set(our_lst))

    # немножечко рекурсии :)
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_pivot = [x for x in arr[1:] if x >= pivot]
            greater_pivot = [x for x in arr[1:] if x < pivot]
            return quick_sort(less_pivot) + [pivot] + quick_sort(greater_pivot)

    # бим-бим бам-бам вот и список :)
    return quick_sort(no_dupl)


if __name__ == "__main__":
    rt = get_sort(lst1, lst2)
    print(rt)
