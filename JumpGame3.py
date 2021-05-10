class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
    
        visited = set()
        def DFS(current):
            
            if current in visited or current <0 or current >=len(arr):
                return False
            visited.add(current)
            
            
            if arr[current]==0:
                return True
            return DFS(current+arr[current]) or DFS(current - arr[current])            
        return DFS(start)