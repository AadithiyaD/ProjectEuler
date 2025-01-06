from functools import reduce
from math import sqrt,floor

def TriNum(n):
    triNum = (n*(n+1))//2

    return triNum


def factors(n):
    factores = set(reduce(list.__add__,([i, n//i] for i in range(1 , floor(sqrt(n)) + 1) if n % i == 0) ))

    length_fact = len(factores)


    return factores,length_fact


over500 = False
x = 1
length_fact_great = 0

while over500 == False:
    factores, length_fact = factors(TriNum(x))

    if length_fact > 500:
        print(factores, length_fact, TriNum(x))
        over500 = True
        break
    elif length_fact >= length_fact_great:
        length_fact_great = length_fact
        print("currently at:",x)
    
    x += 1

