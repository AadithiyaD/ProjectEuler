'''
Same as prob18, but the triangle is now 15k rows
'''

from prob18 import pyramidSum


with open('PythonAttempts/prob67_tri.txt', 'r') as file:
    pyramid = [list(map(int, line.split())) for line in file]

print(pyramidSum(pyramid))