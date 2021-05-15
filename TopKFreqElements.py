class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        ans=[]
        m=Counter(nums)
        print(m)
        s=sorted(m,key=m.get, reverse = True)
        return s[:k]
