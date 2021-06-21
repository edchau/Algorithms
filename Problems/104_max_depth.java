/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        return count(root, 0);
    }
    
    public int count(TreeNode root, int depth) {
        if (root == null) {
            return depth;
        }
        int left = 0;
        int right = 0;
        if (root.left != null)
            left = count(root.left, depth+1);
        if (root.right != null)
            right = count(root.right, depth+1);
        return Math.max(left+1, right+1);
    }
}