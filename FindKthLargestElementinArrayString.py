class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = []

        for n in nums:
           minHeap.append(int(n)* -1)

        heapq.heapify(minHeap)
        while k > 1:
            heapq.heappop(minHeap)

            k -= 1
        return (str(minHeap[0] * -1))
