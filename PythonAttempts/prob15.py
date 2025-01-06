'''
to finish a nxn grid, 2n moves need to be made : n down, and n right

Therefore the question is to find out how many ways these 2n moves can be arranged in an nxn grid

In other words, calculate n C k = n!/(n!)(n-k)!, therefore here: 2n C n = 2n!/(n!)(n!)

'''

from math import factorial
n = 20
print(factorial(2*n)//(factorial(n)*(factorial(n))))