class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        arr = []
        sum = 0
        for i in nums:
            sum += i
            arr.append(sum)

        return arr