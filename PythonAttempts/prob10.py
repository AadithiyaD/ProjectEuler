def sum_of_primes(limit):
    # Create a boolean array to mark primes
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime. If sieve[i] == True => sieve[i] is prime
            # Therefore multiples of sieve[i] i.e i*i must be composite
            for j in range(i * i, limit, i):
                sieve[j] = False

    # Sum up all the primes
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Sum of primes less than 2 million
limit = 2000000
result = sum_of_primes(limit)
print("Sum of primes less than 2 million:", result)
