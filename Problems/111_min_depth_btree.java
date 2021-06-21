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
    /**
    111. Minimum Depth of Binary Tree
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along 
    the shortest path from the root node down to the 
    nearest leaf node.

    Note: A leaf is a node with no children.

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.
    **/
    public int minDepth(TreeNode root) {
        if(root == null) {
            return 0;
        }
        return minDepthFind(root, 1);
    }
    
    private int minDepthFind(TreeNode root, int depth) {
        if (root.left == null && root.right == null) {
            return depth;
        }
        int minLeft = 9999; //make Math.max
        int minRight = 9999;
        if(root.left != null) {
            minLeft = minDepthFind(root.left, depth+1);
        }
        if(root.right != null) {
            minRight = minDepthFind(root.right, depth+1);
        }
        return Math.min(minLeft, minRight);
    }
}