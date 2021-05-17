class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            if nums.count(i) ==1:
                sum+=i
        return sum