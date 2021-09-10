""" Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Start: Sep/04/2021 8:20pm
End: Sep/04/2021 11:30pm
"""

# alternative
def compute2(max):
    sum = 0
    # loop i to 999
    for i in range(max):
        # check if i divisible by 3 or 5, add to sum
        if i % 3 == 0 or i % 5 == 0:
            sum += i

def compute(max):
    # loop i to 999, check if i divisible by 3 or 5, add to list, then sum list 
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

print(f"Sum of All the Multiples of 3 or 5 Is {compute(1000)}")