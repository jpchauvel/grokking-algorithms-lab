from typing import List


def library_sort_epsilon_1(array: List) -> List:
    return _library_sort(array, 1)


def library_sort_epsilon_2(array: List) -> List:
    return _library_sort(array, 2)


def library_sort_epsilon_3(array: List) -> List:
    return _library_sort(array, 3)


def library_sort_epsilon_4(array: List) -> List:
    return _library_sort(array, 4)


def _library_sort(array: List, epsilon: int) -> List:
    array_len = len(array)
    copy = [None] * (1 + epsilon) * array_len
    copy[0] = array[0]
    last_insert_index = 0
    inserted = index = 1
    while inserted < array_len:
        round_inserts = inserted
        while inserted < array_len and round_inserts > 0:
            insertion_index = _binary_search(
                copy, array[index], 0, last_insert_index
            )
            last_insert_index = _insert(
                copy, array[index], insertion_index, last_insert_index
            )
            round_inserts -= 1
            inserted += 1
            index += 1
        last_insert_index = _balance(copy, epsilon, inserted, last_insert_index)
    return [x for x in copy if x is not None]


def _binary_search(array: List, element: int, start: int, end: int) -> int:
    mid = start + ((end - start) // 2)
    if start == end:
        if array[mid] is not None and array[mid] <= element:
            return mid + 1
        else:
            return mid
    else:
        m = mid
        while m < end and array[m] is None:
            m += 1
        if m == end:
            if array[m] is not None and array[m] <= element:
                return m + 1
            else:
                return _binary_search(array, element, start, mid)
        elif m == start:
            if array[m] > element:
                return m
            else:
                return _binary_search(array, element, m + 1, end)
        else:
            if array[m] == element:
                return m + 1
            elif array[m] > element:
                return _binary_search(array, element, start, m - 1)
            else:
                return _binary_search(array, element, m + 1, end)


def _insert(
    array: List, element: int, index: int, last_insert_index: int
) -> int:
    if array[index] is None:
        array[index] = element
    else:
        while array[index] is not None:
            array[index], element = element, array[index]
            index += 1
        array[index] = element
        index += 1
    if index > last_insert_index:
        return index
    return last_insert_index


def _balance(
    array: List, num_spaces: int, total_inserted: int, last_insert_index: int
) -> int:
    queue = [None] * len(array)
    inserted = index = 1
    top = bottom = 0
    while inserted < total_inserted:
        spaces = 0
        while spaces < num_spaces:
            if array[index] is not None:
                queue[bottom] = array[index]
                bottom += 1
            array[index] = None
            index += 1
            spaces += 1
        if array[index] is not None:
            queue[bottom] = array[index]
            bottom += 1
        array[index] = queue[top]
        index += 1
        top += 1
        inserted += 1
    return index - 1
