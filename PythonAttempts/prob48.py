'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^{10} = 385.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^{1000}.
'''

summa = 0

for n in range(1,1001):
    summa += n**n
    print(n)

summa_str = str(summa)
last_10 = summa_str[-10:]
print(summa_str)    
print(last_10)