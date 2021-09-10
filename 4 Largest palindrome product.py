""" Problem 4
Start: Sep/09/2021 6:40pm
Finished: Sep/09/2021 11:40pm
"""
def is_palindrome(x):
    x = str(x)
    # check if string reversed is the same
    if x[::-1] == x:
        return True
    return False

# alternative
def compute2(n):
    # highest and lowest a n digit number can be
    upper = 10**n
    lower = 10**(n-1)

    # loop all 3 digits i and j, check if i*j is palindrome, add to list, then return max list
    return max(i*j
    for i in reversed(range(lower, upper))
    for j in reversed(range(lower, upper))
    if is_palindrome(i*j))

def compute(n):
    # highest and lowest a n digit number can be
    upper = 10**n
    lower = 10**(n-1)
    max_prdct = 0

    for i in reversed(range(lower, upper)):
        # no need to loop numbers already looped by i
        for j in reversed(range(lower, i)):
            prdct = i*j
            # break if prdct is smaller than max_prdct since j is decrementing, prdct will only get smaller each loop
            if prdct < max_prdct:
                break
            if str(prdct)[::-1] == str(prdct):
                max_prdct = prdct
                # break since j is decrementing, largest possible palindrome in already found
                break
    return max_prdct

n = 3
print(f"Largest Palindrome Made From {n}-Digits Is: {compute(n)}")