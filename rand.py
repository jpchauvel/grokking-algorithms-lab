import random


def randomized_list(n, lower_bound, upper_bound):
    lst = []
    for _ in range(n):
        min_val = random.randint(-lower_bound, lower_bound)
        max_val = random.randint(n + min_val, upper_bound)
        lst.append(random.randint(min_val, max_val))
    return lst
