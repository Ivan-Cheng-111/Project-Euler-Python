""" Problem 17
Start: Sep/13/2021 9:40pm
Finished: Sep/14/2021 10:40pm
"""

def compute(lower, upper):
    return sum(num_to_eng(num) for num in range(lower, upper+1))

def num_to_eng(num):
    NUMS_0_TO_9 = [len("zero"),len("one"),len("two"),len("three"),len("four"),len("five"),len("six"),len("seven"),len("eight"),len("nine")]
    NUMS_10_TO_19 = [len("ten"),len("eleven"),len("twelve"),len("thirteen"),len("fourteen"),len("fifteen"),len("sixteen"),len("seventeen"),len("eighteen"),len("nineteen")]
    TENTH_PREFIX = [len("twenty"),len("thirty"),len("forty"),len("fifty"),len("sixty"),len("seventy"),len("eighty"),len("ninety")]
    total = 0

    active_ten_one_digit = False
    digits = list(map(int,str(num)))
    num_of_digits = len(digits)
    # check for 10-19
    if num_of_digits > 1 and digits[-2] == 1:
        active_ten_one_digit = True
        total += NUMS_10_TO_19[digits[-1]]
    # check for 20+
    elif num_of_digits > 1 and digits[-2] > 1:
        active_ten_one_digit = True
        total += TENTH_PREFIX[digits[-2]-2]
        if digits[-1]:
            total += NUMS_0_TO_9[digits[-1]]
    # check for first digit
    elif digits[-1]:
        active_ten_one_digit = True
        total += NUMS_0_TO_9[digits[-1]]

    # 100 digit
    if num_of_digits > 2 and digits[-3]:
        # len("hundred") = 7
        total += NUMS_0_TO_9[digits[-3]] + 7
    
    # 1_000 digit
    if num_of_digits > 3 and digits[-4]:
        # len("thousand") = 8
        total += NUMS_0_TO_9[digits[-4]] + 8
    
    # check if "and" needed
    if num_of_digits > 2 and active_ten_one_digit:
        # len("and") = 3
        total += 3
    return total

lower = 1
upper = 1000
print(f"The Number of Letters Used Between {lower} and {upper} Is: {compute(lower, upper)}")