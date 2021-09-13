""" Problem 16
Start: Sep/13/2021 9:35pm
Finished: Sep/13/2021 9:40pm
"""

def compute(pw):
    num = 2**pw
    digits = list(map(int,str(num)))
    return sum(digits)

n = 1000
print(f"The Sum of the Digits of the Number 2^{n} Is: {compute(n)}")