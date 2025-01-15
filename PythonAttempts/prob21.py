'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than $n$ which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220
Evaluate the sum of all the amicable numbers under 10000.
'''

# Function to calculate sum of proper divisors of n
def sumOfFactors(n):
    results = []
    for i in range(1,n):
        if n % i == 0:
            results.append(i)
    
    return sum(results)

# Function to calculate amicable pairs upto "limit"
def amicable_pair(limit):
    results = []
    
    # Add +1 to include "limit"
    for a in range(limit+1):
        b = sumOfFactors(a)

        # Using the definition provided in problem statement
        if a != b and a == sumOfFactors(b):
            results.append(a)
            results.append(b)
        

    # Returning sorted list for better visualization of results
    return sorted(set(results))

print(amicable_pair(10000))

print(sum(amicable_pair(10000)))
    