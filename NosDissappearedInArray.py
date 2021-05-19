class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        x = list(set(range(1, len(nums)+1)) - set(nums))
        return x 
            
            
            
                
            