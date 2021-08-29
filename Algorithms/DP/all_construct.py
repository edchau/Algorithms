"""
Write a function that takes a target string and an
array of strings. Return a 2D array containing all
of the ways target can be constructed by concatenating
elements from the array of strings. Elements may be reused.

Reminder: branching factor ^ depth

m = target.length
n = word_bank.length

Brute Force:
O(n^m) Time exp overpowers other factors
O(m) Space Height is very large so don't include size of result

Memoization:
O(n^m) Time exp overpowers other factors
O(m) Height is very large so don't include size of result

Tabulation:
O(n^m) Time exp overpowers other factors
O(n^m) 
"""

def all_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            combinations = all_construct(suffix, word_bank, memo)
            target_comb = [[word] + c for c in combinations]
            result += target_comb
    memo[target] = result
    return result

def all_construct_tab(target, word_bank):
    dp = [[] for _ in range(len(target)+1)]
    dp[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:].find(word) == 0:
                dp[i + len(word)] += [arr + [word] for arr in dp[i]]

    return dp[len(target)]


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {}))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee'], {}))

print(all_construct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
    ['e', 'ee', 'eee', 'eeeee', 'eeeeee']))

