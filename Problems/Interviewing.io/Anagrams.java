/**
Sort Anagrams

Veeva Interview

["z", "abc", "bca", "a b c"]
-> ["abc", "bca", "a b c", "z"]
**/

import java.util.*;

public class Anagrams {
    public static void main(String[] args) {
        List<String> words = new ArrayList<>();
        words.add("z");
        words.add("abc");
        words.add("bca");
        words.add(" a b c");
        List<String> result = sortAnagrams(words);
        System.out.println(result.toString());
    }

    public static List<String> sortAnagrams(List<String> words) {
        Collections.sort(words, new Comparator<String>() {
            public int compare(String s1, String s2) {
                s1 = s1.replaceAll("[^a-zA-Z]", "").toLowerCase();
                s2 = s2.replaceAll("[^a-zA-Z]", "").toLowerCase();
                if (s1.length() == s2.length()) {
                    HashMap<Character, Integer> count1 = new HashMap<>();
                    HashMap<Character, Integer> count2 = new HashMap<>();
                    for (int i = 0; i < s1.length(); ++i) {
                        char char1 = s1.charAt(i);
                        char char2 = s2.charAt(i);
                        count1.put(char1, count1.getOrDefault(char1, 0) + 1);
                        count2.put(char2, count2.getOrDefault(char2, 0) + 1);
                    }
                    if (count1.equals(count2)) {
                        return 0;
                    }
                }
                return s1.compareTo(s2);
            }
        });
        return words;
    }
}