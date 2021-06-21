class Solution {
    /**
    ZigZag Conversion

    P   A   H   N
    A P L S I I G
    Y   I   R
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Approach: Store each row as an item in HashMap
    **/
    public String convert(String s, int numRows) {
        if (s.length() < numRows || numRows == 1) {
            return s;
        }
        HashMap<Integer, String> chars = new HashMap<>();
        int pos = 1;
        int sign = 1;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            chars.put(pos, !chars.containsKey(pos) ? Character.toString(c) : chars.get(pos) + c);
            pos += sign;
            if (pos == numRows || pos == 1) {
                sign *= -1;
            }
        }
        System.out.println(chars.toString());
        String converted = "";
        for (int i = 1; i <= numRows; ++i) {
            converted += chars.get(i);
        }
        return converted;
    }
}