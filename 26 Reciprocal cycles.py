""" Problem 26
Start: Sep/15/2021 7:00pm
Finished: Sep/17/2021 10:45pm
"""

import itertools

def cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        seen[x] = i
        x = x * 10 % n


def compute(n):
    return max(range(1,n+1),key=cycle_len)

print(compute(1000))