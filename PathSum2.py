'''
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, sum_tot, lst, result):
        if root.left is None and root.right is None:
            if root.val == sum_tot:
                result += [lst + [root.val]]
        if root.left:
                self.helper(root.left, sum_tot - root.val, lst+[root.val], result)
        if root.right:
                self.helper(root.right, sum_tot - root.val, lst+[root.val], result)
                
        return result   
        
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root, targetSum, [], [])



'''
Runtime: 44 ms, faster than 76.63% of Python3 online submissions for Path Sum II.
Memory Usage: 18.9 MB, less than 41.67% of Python3 online submissions for Path Sum II.
'''
