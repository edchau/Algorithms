class Trie:
    def __init__(self):
        # initial pointer
        self.root = {}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node["*"] = "*"
        
    def common_prefix(self, word):
        lcp = ""
        curr = self.root
        for char in word:
            if char in curr and len(curr) == 1:
                lcp += char
                curr = curr[char]
        return lcp

class Solution:
    # 
    #     Write a function to find the longest common prefix string amongst an array of strings.

    #     If there is no common prefix, return an empty string "".

    #     Example 1:

    #     Input: strs = ["flower","flow","flight"]
    #     Output: "fl"
    #     Example 2:

    #     Input: strs = ["dog","racecar","car"]
    #     Output: ""
    #     Explanation: There is no common prefix among the input strings.
    #  
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.add_word(word)
        
        return trie.common_prefix(strs[0])
    
