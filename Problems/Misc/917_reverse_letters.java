/**
 * Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
 * 
 */
class Solution {
    public String reverseOnlyLetters(String s) {
        int i = 0;
        int j = s.length()-1;
        
        char[] reverse = new char[s.length()];
        while (i <= j) {
            if (!Character.isLetter(s.charAt(i))) {
                reverse[i] = s.charAt(i);
                i++;
            } else if (!Character.isLetter(s.charAt(j))) {
                reverse[j] = s.charAt(j);
                j--;
            } else {
                reverse[i] = s.charAt(j);
                reverse[j] = s.charAt(i);
                i++;
                j--;
            }
        }
        return String.valueOf(reverse);
    }
}