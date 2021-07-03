'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        return self.dfs(root, targetSum, 0)

        
    def dfs(self, root, targetSum, total):
        if not root:
            return False

        total += root.val
        #print(total)

        if not root.left and not root.right:
            return total == targetSum

        return self.dfs(root.left, targetSum, total) or self.dfs(root.right, targetSum, total)
        
        
