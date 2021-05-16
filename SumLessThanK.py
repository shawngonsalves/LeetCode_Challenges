class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        hello = []
        final = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):

                hello.append(nums[i] + nums[j])
        for i in hello:
            if i < k:
                final.append(i)
        if final == []:
            return -1
        else:
            return (max(final))
