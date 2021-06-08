class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r = len(nums)-1
        
        
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        
        while l<=r:
            
            m = l+(r-l)//2
            
            if nums[m] >= target:
                
                if nums[m]==target:
                    return m
                else:
                    if nums[m-1] < target:
                        return m
                    else:
                        r=m-1
            else:
                l = m+1