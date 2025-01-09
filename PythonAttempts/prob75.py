'''
# Right triangles with integer coordinates
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

## Examples
* **12 cm**: (3,4,5)
* **24 cm**: (6,8,10)
* **30 cm**: (5,12,13)
* **36 cm**: (9,12,15)
* **40 cm**: (8,15,17)
* **48 cm**: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

## Examples
* **120 cm**: (30,40,50), (20,48,52), (24,45,51)

# Problem
Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

# Solution:
# We're asked to find out pythagorean triplets that give a unique sum

from math import gcd

def my_func(limit):
    unique_sum = {}

    for m in range(2, int((limit//2)**0.5) + 1):
        for n in range(1,m):
            if (m-n) % 2 == 1 and gcd(m,n) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                triplet_sum = a+b+c

                k = 1 # Scaling factor to get triplet sums og [3 4 5] [ 6 8 10] ...
                while k*triplet_sum <= limit:
                    scaled_sum = k*triplet_sum
                    if scaled_sum in unique_sum:
                        unique_sum[scaled_sum] += 1

                    else:
                        unique_sum[scaled_sum] = 1
                    
                    k += 1
                
    unique_count = sum(1 for count in unique_sum.values() if count == 1)

    return unique_count




print(my_func(1500000))


