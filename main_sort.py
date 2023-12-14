#!/usr/bin/env python3
import argparse
import datetime
import importlib
from typing import List

from rand import randomized_list


def config_arguments():
    parser = argparse.ArgumentParser(
        description="calls a sort function from a given module, builds a"
        " randomized list of integers from the optional parameters and print th"
        " time spent to sort said list."
    )
    parser.add_argument(
        "-m",
        "--module",
        dest="module",
        help="Module of the sort function.",
        required=True,
    )
    parser.add_argument(
        "-f", "--function", dest="function", help="Sort function.", default=None
    )
    parser.add_argument(
        "-l",
        "--low",
        dest="lower_bound",
        help="Randomized list's lower bound",
        type=int,
        default=50000,
    )
    parser.add_argument(
        "-u",
        "--upper",
        dest="upper_bound",
        help="Randomized list's upper bound",
        type=int,
        default=100000,
    )
    parser.add_argument(
        "-s",
        "--size",
        dest="size",
        help="Randomized list's size",
        type=int,
        default=1000,
    )
    return parser


def get_sort_func(module: str, function: str):
    return getattr(importlib.import_module(module), function or module)


def main():
    parser = config_arguments()
    args = parser.parse_args()
    array = randomized_list(args.size, args.lower_bound, args.upper_bound)
    sort = get_sort_func(args.module, args.function)
    start = datetime.datetime.now()
    sort(array)
    duration = (datetime.datetime.now() - start).microseconds
    print(f"{args.function or args.module}: {duration/100} ms")


if __name__ == "__main__":
    main()
