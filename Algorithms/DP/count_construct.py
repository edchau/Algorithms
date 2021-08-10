""" 
Write a function that takes a target string and an
array of strings. Return the number of ways that the
target can be constructed by concatenating elements of
the given string array. Elements may be reused.


Reminder: branching factor ^ depth

m = target.length
n = word_bank.length

Brute Force:
O(n^m * m) Time
O(m * m) Space

Memoization:
O(n * m * m) Time
O(m * m) Space 

Tabulation:
O(n * m * m) Time
O(m) Space
"""

def count_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]

    if target == '':
        return 1
    
    total_count = 0
    for word in word_bank:
        if target.find(word) == 0:
            num_ways = count_construct(target[len(word):], word_bank, memo)
            total_count += num_ways
    memo[target] = total_count
    return total_count


def count_construct_tab(target, word_bank):
    db = [0 for _ in range(len(target)+1)]
    db[0] = 1

    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:].find(word) == 0:
                db[i + len(word)] += db[i]

    return db[len(target)]


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeee'], {}))

print(count_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeee']))
print(count_construct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
