def findNthPrime(n):

    primes = [2]  # Start with the first prime number
    i = 3         # Start checking from 3

    while len(primes) < n:  
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Check divisors up to sqrt(i)
            if i % j == 0:  # If divisible, not a prime
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1  # Check next number

    return primes[-1]


