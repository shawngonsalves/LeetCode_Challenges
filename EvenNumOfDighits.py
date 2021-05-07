class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i >= 10 and i < 100:
                count += 1
            if i >=1000 and i < 10000:
                count+=1
            if i >= 100000 and i < 1000000:
                count+=1
        return count