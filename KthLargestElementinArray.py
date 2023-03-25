class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums)
        l = len(nums)
        return res[l-k]
#nlogn for sort

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = nums
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
            
        
        return minHeap[0]
# n for sort PLUS + k*logn for k pops
