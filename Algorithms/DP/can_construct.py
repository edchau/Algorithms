"""
Write a function that takes a target string and an
array of strings. Return whether or not the target 
can be constructed by concatenating elements in the
given strings array. Elements may be reused.

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

def can_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False


def can_construct_tab(target, word_bank):
    db = [False for _ in range(len(target)+1)]
    db[0] = True

    for i in range(len(target) + 1):
        if db[i]:
            for word in word_bank:
                if target[i:].find(word) == 0:
                    db[i + len(word)] = True
                    
    return db[len(target)]

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {}))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeee'], {}))

print(can_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct_tab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeee']))
