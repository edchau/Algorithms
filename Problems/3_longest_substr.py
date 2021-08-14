class Solution(object):
    """
    Longest Substring Without Repeating Characters

    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        max_length = index = count = 0
        for curr, i in enumerate(s):
            if i not in letters:
                count += 1
            else:
                if letters[i] >= index:
                    count = curr - letters[i]
                    index = letters[i] + 1
                else:
                    count+=1
            # print(i, letters, count)
            max_length = max(max_length, count)
            letters[i] = curr

        return max_length 
