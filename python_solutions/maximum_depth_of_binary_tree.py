# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def maxDepth(node): # Exit condition, return -1 if this is the bottom of the tree
            if node is None:
                return -1 ; 
 
            else: # If not at the bottom, attempt calculating the depth of the tree where the current node is the root
                lDepth = maxDepth(node.left)
                rDepth = maxDepth(node.right)
 
                if (lDepth > rDepth): # Tally up the depth of each branch of the tree steming from the current root node
                    return lDepth + 1
                else:
                    return rDepth + 1
 
        root = TreeNode(1) # Save a reference to the original root node
        root.left = TreeNode(2)     # Assign left and right nodes to the corresponding variables for easier identification
        root.right = TreeNode(3)    # 
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        return maxDepth(root)   # Recursively call the function until all branches of the binary tree were explored up to 'null' values
    
            
        """
        1. If tree is empty then return 0
        2. Else
     (a) Get the max depth of left subtree recursively  i.e., 
          call maxDepth( tree->left-subtree)
     (a) Get the max depth of right subtree recursively  i.e., 
          call maxDepth( tree->right-subtree)
     (c) Get the max of max depths of left and right 
          subtrees and add 1 to it for the current node.
         max_depth = max(max dept of left subtree,  
                             max depth of right subtree) 
                             + 1
     (d) Return max_depth
        """

        
        # Todo: in certain situation code returns results off by 1, needs investigating

