"""
Create Trie given list of words

space	O(n * k), k is length of longest word
insert	O(k)
lookup	O(k)
"""

class Trie:
    def __init__(self):
        # initial pointer
        self.root = {"*":"*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node["*"] = "*"

    def word_exists(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return "*" in curr_node



trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]

for word in words:
    trie.add_word(word)

print(trie.word_exists("wait")) # True
print(trie.word_exists("waite")) # False
print(trie.word_exists("")) # True
print(trie.word_exists("shop")) # True
print(trie.word_exists("shopp")) # False
