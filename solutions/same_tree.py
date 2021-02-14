# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        
        if p is None and q is None: # Check if both binary trees are empty
            return True
        
        if p is None or q is None: # Check if trees are unbalances, i.e. if p has a value where q doesn't
            return False
        
        if p.val != q.val: # Compare the numerical values of both trees
            return False
        
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):   # Recursively call the function to check all
            return True                                                             # corresponding tree nodes until an exception
                                                                                    # is found or the tree is depleted
