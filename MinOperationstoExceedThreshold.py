'''

'''

class Solution:
    def threshold(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, x in enumerate(nums):
            if x >= k:
                return i
            else:
                return len(nums)