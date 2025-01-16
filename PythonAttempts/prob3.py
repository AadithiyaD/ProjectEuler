'''
What is the largest prime factor of the number 600851475143
'''

n = 600851475143
i = 3

while i * i <= n: # Checking factors upto square root of n
    while n % i == 0: # Checking if i is a Prime factor
        n = n // i # Removing this factor from the number by integer dividing

    i += 2 # Checking next prime number

# Code works on the basis that all prime numbers except 2 are odd, the given number is not even so start with 3
# After all divisions, we're left with the largest prime factor

print(n)