class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for ef, sp in zip(efficiency, speed):
            eng.append([ef, sp])
        eng.sort(reverse = True)
        minHeap, res, speed = [], 0, 0

        for ef, sp in eng:
            if len(minHeap) == k:
                speed -= heapq.heappop(minHeap)
            speed +=sp
            heapq.heappush(minHeap, sp)
            res = max(res, ef * speed)

        return res %(10**9 + 7)
