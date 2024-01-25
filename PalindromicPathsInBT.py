'''

LC: 1457
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0

        def inorder(cur):
            nonlocal odd # this tells python we are not decraling new val, we are using global
            if not cur:
                return 0
            
            count[cur.val] += 1
            odd_change = 1 if count[cur.val] % 2 == 1 else -1 # look at 2-> 3 -> 3 and try to map it, if we encounter 1st 3 we get odd == 2 and then on 2nd occurence of 3 we decrement odd and that becomes 1 again
            odd += odd_change

            if not cur.left and not cur.right:
                res = 1 if odd <= 1 else 0
            else:
                res = (inorder(cur.left) + inorder(cur.right))            
            odd -= odd_change
            count[cur.val] -= 1
            return res

            

        return inorder(root)
    
'''
Runtime 338 ms Beats 75.88% of users with Python3
Memory 43.30 MB Beats 82.44% of users with Python3
'''