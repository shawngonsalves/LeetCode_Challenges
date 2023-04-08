# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            inorder(root.right)
            res.append(root.val)
        inorder(root)
        return res
