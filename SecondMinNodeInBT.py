# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

 

 

# Example 1:


# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:


# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 231 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        nums = []
        nodes = [root]

        while nodes:
            t = nodes.pop()
            nums.append(t.val)
            if t.left:
                nodes.append(t.left)
            if t.right:
                nodes.append(t.right)
        if len(set(nums)) == 1:
            return -1
        return sorted(set(nums))[1]

# Runtime 33 ms Beats 91.71%
# Memory 16.4 MB Beats 34.35%