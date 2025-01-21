'''
Euler discovered the remarkable quadratic formula: n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
 n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n = 0.

'''
from math import isqrt

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
        
    return True

def coeff_find():
    best_a = 0
    best_b = 0
    primes_max = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0

            while True:
                formula_result = n**2 + a*n + b

                if not is_prime(formula_result): # If is_prime() returns false, meaning the number is composite, this gets executed
                    break

                n += 1
            
            if n > primes_max:
                primes_max = n
                best_a = a
                best_b = b
    
    return primes_max, best_a, best_b

max_primes, a, b = coeff_find()
print(a*b)

