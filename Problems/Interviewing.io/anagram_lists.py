"""
Given
List of Strings
Input String

Return True/False if anagram for input string is in list of strings
"""
# // result[]
# // words - input_words = n
# // length of longest word in m
def find_anagram_in_list(words, input_words):
  
  words_set = set()
  for word in words:
    freq = {}
    for ch in word:
      freq[ch] = freq.get(ch, 0) + 1
    
    val = ""
    for key in sorted(list(freq.keys())):
      val += key + str(freq[key])
    words_set.add(val)
    
  result = []
  for word in input_words:
    freq = {}
    for ch in word:
      freq[ch] = freq.get(ch, 0) + 1
    
    val = ""
    for key in sorted(list(freq.keys())):
      val += key + str(freq[key])
    
    if val in words_set:
      result.append(True)
    else:
      result.append(False)
  
  return result

# True True False
print(find_anagram_in_list(["aba", "bca", "eee"], ["abc", "baa", "cbe"]))

# False False False
print(find_anagram_in_list(["aba", "bca", "eee"], ["abcc", "baaa", "cbe"]))  
 
 
  # freq_input = []
  # result = [False] * len(input_words)
  
  # for i, input_word in enumerate(input_words):
  #   for ch in input_word:
  #     freq_input[ch] = freq_input.get(ch, 0) + 1
    
      
  # for word in words:
  #   word_freq = {}
  #   for ch in word:
  #     word_freq[ch] = word_freq.get(ch, 0) + 1
      
      
      # # check if maps are equal
      # if word_freq == freq_input:
      #   result[i] = True
      
# input_words  
# set("aba", "abc", "bbe")
# words
# set("hello", "table", "baa")


#aba -> {a:2, b:1} {a:2, b:1}

#                  {b:1, c:1, a:1}
#abc -> {a:1, b:1, c:1} {b:2 a:1} , {b:1, c:1, a:1} true
    
# print(find_anagram_in_list(["aba", "abc", "bbe"], "bcaa")) # True
# print(find_anagram_in_list(["aba", "abc", "bbe"], "ccd")) # False
