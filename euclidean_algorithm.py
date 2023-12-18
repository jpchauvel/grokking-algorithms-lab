#!/usr/bin/env python3
def gcd(a: int, b: int):
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a % b)


def main():
    print(gcd(270, 192))


if __name__ == "__main__":
    main()
