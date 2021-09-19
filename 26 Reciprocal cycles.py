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


def compute(d):
    return max(range(1,d+1),key=cycle_len)

d = 1000
print(f"The Value of 1/d <{d} Containing the Longest Recurring Cycle Is: {compute(d)}")