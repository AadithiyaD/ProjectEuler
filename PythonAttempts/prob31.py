'''
Find out number of ways to make 2pounds from the currency in circulation in british currency
'''

def count_ways(target, coins):
    ways = [0] * (target + 1) # Each index represents the number of ways to make that amount with the coin
    ways[0] = 1  # One way to make 0p i.e no coins
    
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
print(count_ways(target, coins))
