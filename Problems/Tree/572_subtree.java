/**
 * Given the roots of two binary trees root and subRoot, return true 
 * if there is a subtree of root with the same structure and node values 
 * of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree 
and all of this node's descendants. The tree tree could also be considered 
as a subtree of itself.
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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return traverse(root, subRoot);
    }
    
    public boolean traverse(TreeNode node, TreeNode subNode) {
        if (node == null) {
            return false;
        }
        boolean equals = false;
        if (node.val == subNode.val) {
            equals = checkEqual(node, subNode);
        }
        
        return equals || traverse(node.left, subNode) || traverse(node.right, subNode);
    }
    
    public boolean checkEqual(TreeNode node, TreeNode subNode) {
        if (node == null && subNode == null) {
            return true;
        }
        if (node == null || subNode == null) {
            return false;
        }
        if (node.val != subNode.val) {
            return false;
        }
        return checkEqual(node.left, subNode.left) && checkEqual(node.right, subNode.right);
    }
}