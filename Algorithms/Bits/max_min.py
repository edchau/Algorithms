"""
Find the max and min between two numbers using
bit manipulation

Key takeaways: xoring with same thing results in nothing
"""


def min(x, y):
     
    return y ^ ((x ^ y) & -(x < y))
 
 
# Function to find maximum of x and y
def max(x, y):
 
    return x ^ ((x ^ y) & -(x < y))
 
 
# Driver program to test above functions
x = 15
y = 6
print("Minimum of", x, "and", y, "is", end=" ")
print(min(x, y))
print("Maximum of", x, "and", y, "is", end=" ")
print(max(x, y))