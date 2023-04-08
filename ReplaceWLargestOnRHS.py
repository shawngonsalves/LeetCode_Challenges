class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        nums = arr

        def getMax(nums):
            return max(nums)

        res = []
        for i in range(len(nums)):
            
            if i == len(nums)-1:
                res.append(-1)
                break
            res.append(getMax(nums[i+1:]))

        return res

        

