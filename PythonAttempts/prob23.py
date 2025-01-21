'''
Find the sum of numbers upto 28123 that cannot be expressed as the sum of two abundant numbers
'''
from math import sqrt

def divisor_sums(n):
    """
    Function to calculate sum of divisors of the number n
    """
    divisors = set()
    divisors.add(1) # In the problem, the number itself is not conted, so we manually add 1 to avoid listing the number itself as
                    # a factor
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i) # If i divides n, then n // i also divides n
    
    return sum(divisors)

def abundant_nums(limit):
    """
    Function to generate a list of abundant numbers up to limit
    :param limit: the upper limit of abundant numbers to generate
    :return: a list of abundant numbers up to limit
    """
    nums = [x for x in range(1,limit + 1) if divisor_sums(x) > x]
    return nums

def abundant_sums(n):
    """
    Function to generate a set of sums of two abundant numbers up to n
    :param n: the upper limit of the abundant number sums to generate
    :return: a set of sums of two abundant numbers up to n
    """
    input_numbers = abundant_nums(limit)
    result = set()
    for i in range(len(input_numbers)):
        for j in range(i, len(input_numbers)):
            s = input_numbers[i] + input_numbers[j]
            if s <= n:
                result.add(s)
            else:
                break

    return result

limit = 28123
all_nums = set(range(1, limit + 1))
answer = sum(all_nums - abundant_sums(limit))

print(answer)
