# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def maxDepth(Root,depth):
            if(Root == None):
                return depth
            else:
                return max(maxDepth(Root.left,depth+1),maxDepth(Root.right,depth+1))
        return maxDepth(root,0)