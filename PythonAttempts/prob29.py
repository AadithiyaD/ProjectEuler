'''
Find out how many distinct numbers can be made when a**b and 2<= a,b <= 100
'''
nums = set()
for a in range(2,101):
    for b in range(2,101):
        nums.add(a**b)
        #print(a**b)

print(len(nums))