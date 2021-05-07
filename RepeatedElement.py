class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        
        m = int(n/2)
        
        for i in A:
            if A.count(i) == m:
                return i