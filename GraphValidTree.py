
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True
        visit = set()
        adj = {i:[] for i in range(n)}


        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            
            for j in adj[i]:
                if j ==prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
