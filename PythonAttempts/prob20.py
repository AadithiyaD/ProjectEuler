'''
n! means = n*(n-1).......

For example, 10! = 10*9*8*7*6*5*4*3*2*1 = 3628800

and the sum of the digits in the number is 3628800 = 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

Find the sum of the digits in the number 100!

'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


ans_str = str(factorial(100))
ans = 0
for i in ans_str:
    ans += int(i)



print(ans_str)
print(ans)