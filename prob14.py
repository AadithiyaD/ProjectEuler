def collatz_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        memo[n] = 1 + collatz_length(n // 2, memo)
    else:
        memo[n] = 1 + collatz_length(3 * n + 1, memo)
    return memo[n]

def longest_collatz(limit):
    memo = {}
    max_length = 0
    number = 0

    for i in range(1, limit):
        length = collatz_length(i, memo)
        if length > max_length:
            max_length = length
            number = i

    return number, max_length

# Find the number under 100,000 with the longest Collatz sequence
limit = 1000000
num, length = longest_collatz(limit)
print(f"The number under {limit} with the longest Collatz sequence is {num}, with a sequence length of {length}.")
