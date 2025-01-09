'''
Euler's totient function phi(n) is number of positive numbers that are relatively prime to n while <= n
i.e phi(9)= 6 as 1,2,4,5,7,8 are relatively prime

find n where n/phi(n) is maximum, while n<= 1 000 000


Too slow, needs to be optimized
'''

from math import gcd

def Totient(n):
    count = 0
    for i in range(1,n):
        if gcd(n,i) == 1:
            count += 1

    return n, count

new_max = 0
for i in range(2,1000001):
    n, phi = Totient(i)

    if (n/phi) > new_max:
        new_max = n/phi
        print("new n =",n)
        print("New maximum is =",new_max)


    
