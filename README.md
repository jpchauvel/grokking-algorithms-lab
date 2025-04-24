Grokking Algorithms lab
=======================

Some own experiments and exercises from the book.

Link to the book: [Grokking Algorithms - Manning](https://www.manning.com/books/grokking-algorithms)


Installation:
```bash
uv sync
```

Usage:
```bash
usage: main_sort.py [-h] -m MODULE [-f FUNCTION] [-l LOWER_BOUND] [-u UPPER_BOUND] [-s SIZE]

calls a sort function from a given module, builds a randomized list of integers from the optional parameters and print the time spent to sort said list.

options:
  -h, --help            show this help message and exit
  -m MODULE, --module MODULE
                        Module of the sort function.
  -f FUNCTION, --function FUNCTION
                        Sort function.
  -l LOWER_BOUND, --low LOWER_BOUND
                        Randomized list's lower bound
  -u UPPER_BOUND, --upper UPPER_BOUND
                        Randomized list's upper bound
  -s SIZE, --size SIZE  Randomized list's size
```

Example 1. Run bubble_sort function from bubble_sort module with an input list of 10k elements:
```bash
uv run ./main_sort.py -m bubble_sort -s 10000 
```

Example 2. Run library_sort_epsilon_4 function from library_sort module with an input list of 20k elements:
```bash
uv run ./main_sort.py -m library_sort -f library_sort_epsilon_4 -s 20000
```
