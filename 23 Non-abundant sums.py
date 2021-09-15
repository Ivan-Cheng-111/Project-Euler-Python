""" Problem 23
Start: Sep/14/2021 9:25pm
Finished: Sep/14/2021 11:35pm
"""

from math import ceil

# sieve of eratosthenes inspired
def compute():
    LIMIT = 28123

    # make list of 0s sized LIMIT
    divisor_sums = [0] * LIMIT
    for n in range(1,ceil(LIMIT/2)):
        for pos in range(n*2,LIMIT,n):
            divisor_sums[pos] += n

    abundant = [n for n,divisor_sum in enumerate(divisor_sums) if n < divisor_sum]
    
    # make boolen list sized LIMIT
    is_not_abundant = [True] * LIMIT

    # mark out all the numbers with sum of abundant numbers
    for n1 in abundant:
        for n2 in abundant:
            sum_of_abundant = n1 + n2
            if sum_of_abundant and sum_of_abundant < LIMIT:
                is_not_abundant[sum_of_abundant] = False
            else:
                break

    # sum marked true (aka the non-abundant numbers)
    return sum(i for i in range(LIMIT) if is_not_abundant[i])

print(f"The Sum of All Numbers Not The Sum of Two Abundant Numbers Is: {compute()}")