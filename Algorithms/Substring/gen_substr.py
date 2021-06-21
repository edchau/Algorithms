"""
Generate all posible substrings algorithm
If needed to find substrings, use aho corasick instead

O(N^2) Time
"""

test_str = 'HELLO'

for i in range(len(test_str)):
    for j in range(i+1, len(test_str)+1):
        print(test_str[i:j])