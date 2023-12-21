from typing import List


def mergesort(array: List) -> List:
    array_len = len(array)
    if array_len <= 1:
        return array

    left = array[:array_len // 2]
    right = array[array_len // 2:]
    left = mergesort(left)
    right = mergesort(right)
    return _merge(left, right)


def _merge(left: List, right: List) -> List:
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    result.extend(left)
    result.extend(right)
    return result
