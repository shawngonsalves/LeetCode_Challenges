class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        m = n
        if n == 1:
            return 1
        for i in range(1,n+1):
            if m - i > 0:
                m -= i
            elif m-i == 0:
                return i
            else:
                return i-1
