class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            ql = len(q)
            for i in range(ql):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
