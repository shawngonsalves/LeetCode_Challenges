'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def get_longest(node):
            if node is None:
                return 0
            nonlocal best
            left = get_longest(node.left)
            right = get_longest(node.right)
            best = max(best, left + right + 1)

            return max(left, right) + 1
        get_longest(root)
        return best - 1
    
'''
Runtime 33 ms Beats 95.88% of users with Python3
Memory 17.68 MB Beats 73.92% of users with Python3
'''