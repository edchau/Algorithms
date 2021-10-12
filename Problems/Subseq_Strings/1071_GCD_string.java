/**
 * For two strings s and t, we say "t divides s" if and only if s = t + ... + t  
 * (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2.

 */

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        String s = str1.length() < str2.length() ? str1 : str2;
        int i = 1;
        while (i <= s.length()) {
            if (s.length() % i != 0) {
                ++i;
                continue;
            }           
            String sub = s.substring(0, s.length() / i);
            if (str1.replace(sub, "").isEmpty() && str2.replace(sub, "").isEmpty()) {
                return sub;
            }
            ++i;
        }
        return "";
    }

}