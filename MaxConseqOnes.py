class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)
        res = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res