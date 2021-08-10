"""
Aho-Corasick Algorithm for String Matching
n is length of text, m is length of keywords
O(n*k + m) Time Complexity where k is total number of input words
Finds words in O(n + m + z) where z is occurences of length m word

failure links: https://www.youtube.com/watch?v=O7_w001f58c
dictionary links: https://www.youtube.com/watch?v=OFKxWFew_L0
"""

class Trie:
    def __init__(self, words):
        self.root = {'fail_link':None, 'dict_link': None}

        # Build Trie
        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['is_word'] = word

        # Calculate Fail Links and Dictionary Links
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            for char in node:
                # ignore non letters in trie
                if len(char)==1:
                    child = node[char]
                    extend = node['fail_link']
                    # follow fail link all the way
                    while extend and not char in extend:
                        extend = extend['fail_link']
                    if extend:
                        # if extend exists, then set that fail link
                        child['fail_link'] = extend[char]
                    else:
                        # otherwise, fail link will be root (for children of self.root)
                        child['fail_link'] = self.root
                    if 'is_word' in child['fail_link']:
                        # if the fail link is a word, then add a dict link
                        child['dict_link'] = child['fail_link']
                    else:
                        # deep copy of dict, not shallow so new dict link copies over
                        child['dict_link'] = child['fail_link']['dict_link']
                    queue.append(child)

    def search_word(self, string):
        extend = self.root
        for char in string:
            # go through fail links if char is not in node
            while extend and char not in extend:
                extend = extend['fail_link']
            if extend:
                # if extend exists, go to the character and check is_word
                extend = extend[char]
                if 'is_word' in extend:
                    print("FOUND ", extend['is_word'], " in ", string)
                if extend['dict_link']:
                    print("FOUND ", extend['dict_link']['is_word'], " in ", string)
                    

print("FAILURE LINK TEST")
print("--------------------")
string = 'GCATCG'
words = ['ACC','ATC','CAT','GCG']
trie = Trie(words)
trie.search_word(string)
print()
print("DICTIONARY LINK TEST")
print('---------------------')
string2 = 'GCAA'
words2 = ['A','AG','C','CAA','GAG','GC','GCA']
trie = Trie(words2)
trie.search_word(string2)