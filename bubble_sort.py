from typing import List


def bubble_sort(array: List) -> List:
    done = False
    array_len = len(array)
    for i in range(array_len):
        done = True
        for j in range(array_len - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                done = False
        if done:
            return array
    return array
