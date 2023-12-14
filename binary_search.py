#!/usr/bin/env python3
def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high + 1) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


def main():
    print(binary_search(list(range(-123943, 501123)), 23))


if __name__ == "__main__":
    main()
