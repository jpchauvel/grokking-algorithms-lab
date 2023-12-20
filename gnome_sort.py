from typing import List


def gnome_sort(array: List) -> List:
    i = 0
    while i < len(array):
        if i == 0 or array[i] >= array[i - 1]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    return array
