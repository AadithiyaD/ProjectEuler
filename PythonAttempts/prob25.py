'''
What is the first fibonacci number to have more than 1000 digits?

F1 = 1
F2 = 1

Fn = F(n-1) + F(n-2)
'''

from math import sqrt

#Fibonacci sequence calculator
def fibo(n):
    a , b = 1,1
    for i in range(2,n):
        a, b = b, a + b
    return i+1, b


new = 0  #initializing current value
x = 12    #Starting from 12 to skip 1 to 11

#Finding the len of current fibo number
while len(str(new)) <= 1000:
    index, new = fibo(x)
    if len(str(new)) == 1000:
        print(f"{index}th number is the first to have 1000 digits")
        break
    
    x += 1
