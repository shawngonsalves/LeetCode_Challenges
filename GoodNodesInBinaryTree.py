'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.


Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.


Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.res = 0
        self.DFS(root, root.val)
        return self.res
    
    def DFS(self, root, cur_max):
        
        if root.val >= cur_max:
            self.res += 1
            cur_max = root.val
        
        if root.left:
            self.DFS(root.left, cur_max)
            
        if root.right:
            self.DFS(root.right, cur_max)
            
'''
Runtime: 224 ms, faster than 97.34% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 33.4 MB, less than 42.02% of Python3 online submissions for Count Good Nodes in Binary Tree.
'''        