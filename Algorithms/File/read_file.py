"""
Read in a file in python

https://www.pythontutorial.net/python-basics/python-read-text-file/
"""

with open('/Users/edward/Desktop/LeetCode/Algorithms/File/test.txt') as f:
    # reads entire file as one string
    print(f.read())

    # read only one line
    print(f.readline())

    # read lines into a list
    print(f.readlines())

    # read in line by line
    for line in f:
        print(line)

# open utf 8 file
with open('quotes.txt', encoding='utf8') as f:
    for line in f:
        # strip beginning and ending spaces
        print(line.strip())