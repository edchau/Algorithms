"""
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory 
buffer, or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # use bfs to get row order
        if root == None:
            return ''
        queue = [root]
        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ','.join(res)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = [root]
        index = 1
        
        while len(queue) > 0:
            # left branch
            node = queue.pop(0)
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            # right branch
            if nodes[index] != '#':                
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        String tree = "";
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (tree.length() != 0) {
                tree += ",";
            } 
            if (node == null) {
                tree += "#";
            } else {
                tree += String.valueOf(node.val);
                queue.add(node.left);
                queue.add(node.right);
            }
        }
        return tree;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        String[] nodes = data.split(",");
        
        TreeNode root = new TreeNode(Integer.valueOf(nodes[0]));
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int index = 1;
        
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            // left subtree
            if (!nodes[index].equals("#")) {
                node.left = new TreeNode(Integer.valueOf(nodes[index]));
                queue.add(node.left);
            }
            index += 1;
            
            // right subtree
            if (!nodes[index].equals("#")) {
                node.right = new TreeNode(Integer.valueOf(nodes[index]));
                queue.add(node.right);
            }
            index += 1;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

"""