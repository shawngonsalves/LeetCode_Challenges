class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1  if  node.val>= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res+= dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)
