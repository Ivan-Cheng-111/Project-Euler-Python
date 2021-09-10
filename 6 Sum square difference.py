""" Problem 6
Start: Sep/10/2021 3:37pm
Finished: Sep/10/2021 4:00pm
"""

# alterante, less efficient ultimate one liner using list comprehensions
def compute2(lower, upper):
    return sum(i for i in range(lower, upper+1))**2 - sum(i**2 for i in range(lower, upper+1))

def compute(lower, upper):
    sum_squares = 0
    sums = 0
    for i in range(lower, upper+1):
        sum_squares += i**2
        sums += i
    return sums**2 - sum_squares

lower, upper = 1, 100
print(f"The Difference Between Sum of Squares and Square of Sums by Numbers Between {lower} and {upper} Is: {compute(lower, upper)}")