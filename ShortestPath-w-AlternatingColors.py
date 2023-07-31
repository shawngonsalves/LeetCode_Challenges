# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
 

# Constraints:

# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n

from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        redAdj = defaultdict(list)
        blueAdj = defaultdict(list)
        redVisit = set()
        blueVisit = set()

        for from_node, to_node in redEdges:
            redAdj[from_node].append(to_node)
        for from_node, to_node in blueEdges:
            blueAdj[from_node].append(to_node)

        res = [-1] * n

        queue = deque([(0, 0)])
        length = 0
        while queue:
            for _ in range(len(queue)):
                node, c = queue.pop()
                if res[node] == -1:
                    res[node] = length

                if c != -1:
                    for neighbor in redAdj[node]:
                        if neighbor not in redVisit:
                            queue.appendleft((neighbor, -1))
                            redVisit.add(neighbor)

                if c != 1:
                    for neighbor in blueAdj[node]:
                        if neighbor not in blueVisit:
                            queue.appendleft((neighbor, 1))
                            blueVisit.add(neighbor)

            length += 1

        return res

# Runtime 93 ms Beats 92.45%
# Memory 16.5 MB Beats 71.13%