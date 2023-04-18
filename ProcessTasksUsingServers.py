class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)

        avail = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(avail)
        unavail = []

        t= 0
        for i in range(len(tasks)):
            t = max(t, i)

            if (len(avail)) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                timefree, weight, index = heapq.heappop(unavail)
                heapq.heappush(avail, (weight, index))
            weight, index = heapq.heappop(avail)
            res[i] = index
            heapq.heappush(unavail, (t + tasks[i], weight, index))
        return res
