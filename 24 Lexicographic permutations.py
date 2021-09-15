""" Problem 24
Start: Sep/15/2021 1:30am
Finished: Sep/15/2021 1:40am
"""

import itertools

n = 1_000_000
digits = [0,1,2,3,4,5,6,7,8,9]
perms = ["".join(i) for i in itertools.permutations("".join(map(str,digits)), len(digits))][n-1]

print(f"The Lexicographic Permutation of the Digits {digits} at {n:_} Is: {perms}")