#!/usr/bin/env python3
from typing import List


def list_sum(array: List) -> int:
    if len(array) == 1:
        return array[0]
    return array[0] + list_sum(array[1:])


def main():
    print(list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10 * (10 + 1) // 2)


if __name__ == '__main__':
    main()
