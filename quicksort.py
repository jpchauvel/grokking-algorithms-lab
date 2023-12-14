from typing import List


def quicksort(array: List) -> List:
    _quicksort(array, 0, len(array) - 1)
    return array


def _quicksort(array: List, low: int, high: int):
    if low >= high or low < 0:
        return
    p = _partition(array, low, high)
    _quicksort(array, low, p - 1)
    _quicksort(array, p + 1, high)


def _partition(array: List, low: int, high: int):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[high] = array[high], array[i]
    return i
