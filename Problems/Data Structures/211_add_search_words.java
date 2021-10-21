/**
 * Design a data structure that supports adding new words and finding 
 * if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure 
that matches word or false otherwise. word may contain dots '.' where dots 
can be matched with any letter.
 * 
 */

class WordDictionary {
    public class TrieNode { 
        public HashMap<Character, TrieNode> children = new HashMap<>();
        public boolean isWord = false;
    }
    
    
    private TrieNode root;
        
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children.get(c) == null) {
                node.children.put(c, new TrieNode());   
            }
            node = node.children.get(c);
        }
        node.isWord = true;
    }
    
    public boolean search(String word) {
        return match(word.toCharArray(), 0, root);
    }
    
    private boolean match(char[] word, int k, TrieNode node) {
        if (k == word.length) {
            return node.isWord;
        }
        if (word[k] == '.') {
            for (char key : node.children.keySet()) {
                TrieNode child = node.children.get(key);
                if (child != null) {
                    if (match(word, k+1, child)) {
                        return true;
                    }
                }
            }
            
        } else {
            TrieNode child = node.children.get(word[k]);
            if (child != null) {
                return match(word, k+1, child);   
            }
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */