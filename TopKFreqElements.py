class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        ans=[]
        m=Counter(nums)
        print(m)
        s=sorted(m,key=m.get)
        print(s)
        for i in range(k,0,-1):
            
            ans.append(s.pop())
            
        return ans