# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        n = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n+=1
            if k == n:
                return curr.val
            curr = curr.right

# Runtime 72 ms Beats 33.25%
# Memory 20.3 MB Beats 77.11%