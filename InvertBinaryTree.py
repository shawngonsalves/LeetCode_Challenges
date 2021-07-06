'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


Example 2:

Input: root = [2,1,3]
Output: [2,3,1]


Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


'''
Runtime: 28 ms, faster than 87.08% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 98.42% of Python3 online submissions for Invert Binary Tree.
'''