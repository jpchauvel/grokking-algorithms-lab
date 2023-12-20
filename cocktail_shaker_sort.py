from typing import List


def cocktail_shaker_sort(array: List) -> List:
    array_len = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(array_len - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(array_len - 2, -1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array
