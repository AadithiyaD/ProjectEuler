'''
Find the max total from top to bottom for the below pyramid
'''

pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

def pyramidSum(pyramid):
    """
    This is a bottom up sum for finding the maximum path sum
    we do row in range(len(pyramid - 2, -1, -1)) => start at second to last row (i.e [63, 66, 4 ...])
    -1 means go upto -1 index, and since range is exclusive of the limit, the loop goes upto index 0
    the other -1 means increments of -1
    what we are doing is looking at the max of the children of one node, and adding the bigger child to the parent node
    ex: for 63, child nodes = 4, 62. 62 is bigger, so 62 is added to 63, and 63 is replaced with 125
    This process is repeated till we go to the top
    """
    for row in range(len(pyramid) - 2, -1, -1):
        for col in range(len(pyramid[row])):
            pyramid[row][col] += max(pyramid[row+1][col], pyramid[row+1][col+1])
    
    return pyramid[0][0]


# We use this to make sure that this part doesnt get executed when importing this script
if __name__ == "__main__":
    print(pyramidSum(pyramid))

# * Using a top down approach would mean we would have to calculate every possible path
# * It would not account for the fact that the numbers beneath a row might be bigger, and make the path sum bigger
# * By starting from the bottom, we imagine the last row to be the "maximum sum" row of the numbers beneath it