class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        l = Counter(A)
        print(l)
        
        res = -1
        print(l.items())
        for i,j in l.items():
            if j==1:
                res = max(res, i)
                
        return res