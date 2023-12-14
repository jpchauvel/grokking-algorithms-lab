from typing import List


def selection_sort(array: List) -> List:
    array_len = len(array)
    for i in range(array_len - 1):
        smallest = i
        for j in range(i + 1, array_len):
            if array[j] < array[smallest]:
                smallest = j
                continue
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
    return array
