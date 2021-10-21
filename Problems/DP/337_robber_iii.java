/**
 * The thief has found himself a new place for his thievery again. There 
 * is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, 
the smart thief realized that all houses in this place form a binary tree. It 
will automatically contact the police if two directly-linked houses were broken 
into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief 
can rob without alerting the police.
 * 
 */


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
    public int rob(TreeNode root) {
        HashMap<TreeNode, Integer> memo = new HashMap<>();
        return maxRob(root, memo);
    }
    
    public int maxRob(TreeNode node, HashMap<TreeNode, Integer> memo) {
        if (node == null) {
            return 0;
        }
        
        if (memo.containsKey(node)) {
            return memo.get(node);
        }
        
        int val = 0;
        
        // skip 1 level because we're robbing current node
        if (node.left != null) {
            val += maxRob(node.left.left, memo) + maxRob(node.left.right, memo);
        }

        if (node.right != null) {
            val += maxRob(node.right.left, memo) + maxRob(node.right.right, memo);
        }
        
        // rob current node and next branches or go to next level
        val = Math.max(node.val + val, maxRob(node.left, memo) + maxRob(node.right, memo));
        
        memo.put(node, val);
        return val;
    }
}