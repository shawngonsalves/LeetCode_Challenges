class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        side = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        
        matchsticks.sort(reverse = True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):

                if side[j] + matchsticks[i] <= length:
                    side[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    side[j] -= matchsticks[i]
            return False
        return backtrack(0)
        
